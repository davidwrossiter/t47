# quick.py with live temperature logging

import sys
import time
import threading

sys.setrecursionlimit(1_000_000)

if len(sys.argv) != 2:
    print("usage: quick.py <datafile>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as f:
    arr = [int(line) for line in f]

n = len(arr)

THERMAL_FILE = "/sys/class/thermal/thermal_zone0/temp"

def read_temp():
    with open(THERMAL_FILE) as f:
        return int(f.read().strip()) / 1000.0

done = threading.Event()
samples = []

def logger():
    t0 = time.monotonic()
    while not done.is_set():
        elapsed = time.monotonic() - t0
        temp = read_temp()
        samples.append((elapsed, temp))
        print(f"\rt={elapsed:6.1f}s  T={temp:5.2f} C", end="", flush=True)
        time.sleep(1.0)

def quicksort(arr, lo, hi):
    if lo < hi:
        pivot = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        p = i + 1
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

log_thread = threading.Thread(target=logger, daemon=True)
log_thread.start()

start = time.monotonic()
quicksort(arr, 0, n - 1)
elapsed = time.monotonic() - start

done.set()
log_thread.join()
print()

print(f"n={n} time={elapsed:.3f}s samples={len(samples)}")

with open("quick_temps.csv", "w") as f:
    f.write("elapsed_s,temp_c\n")
    for t, T in samples:
        f.write(f"{t:.3f},{T:.3f}\n")
print("Wrote quick_temps.csv")
