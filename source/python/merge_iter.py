# merge_iter.py with live temperature logging
# Iterative bottom-up merge sort, avoids recursion limit issues.

import sys
import time
import threading

if len(sys.argv) != 2:
    print("usage: merge_iter.py <datafile>", file=sys.stderr)
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

def merge_sort(arr):
    n = len(arr)
    width = 1
    buf = [0] * n
    while width < n:
        for i in range(0, n, 2 * width):
            left, mid, right = i, min(i + width, n), min(i + 2 * width, n)
            a, b = left, mid
            for k in range(left, right):
                if a < mid and (b >= right or arr[a] <= arr[b]):
                    buf[k] = arr[a]
                    a += 1
                else:
                    buf[k] = arr[b]
                    b += 1
        arr[:] = buf[:n]
        width *= 2

log_thread = threading.Thread(target=logger, daemon=True)
log_thread.start()

start = time.monotonic()
merge_sort(arr)
elapsed = time.monotonic() - start

done.set()
log_thread.join()
print()

print(f"n={n} time={elapsed:.3f}s samples={len(samples)}")

with open("merge_temps.csv", "w") as f:
    f.write("elapsed_s,temp_c\n")
    for t, T in samples:
        f.write(f"{t:.3f},{T:.3f}\n")
print("Wrote merge_temps.csv")
