# heap.py with live temperature logging

import sys
import time
import threading

if len(sys.argv) != 2:
    print("usage: heap.py <datafile>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as f:
    arr = [int(line) for line in f]

n = len(arr)

THERMAL_FILE = "/sys/class/thermal/thermal_zone0/temp"

def read_temp():
    with open(THERMAL_FILE) as f:
        return int(f.read().strip()) / 1000.0

# Shared state between the sort and the logger.
done = threading.Event()
samples = []  # list of (elapsed_seconds, temp_celsius)

def logger():
    t0 = time.monotonic()
    while not done.is_set():
        elapsed = time.monotonic() - t0
        temp = read_temp()
        samples.append((elapsed, temp))
        # \r returns to start of line, end="" suppresses newline,
        # flush=True forces immediate output.
        print(f"\rt={elapsed:6.1f}s  T={temp:5.2f} C", end="", flush=True)
        time.sleep(1.0)

def sift_down(arr, start, end):
    root = start
    while 2 * root + 1 <= end:
        child = 2 * root + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

def heapsort(arr):
    n = len(arr)
    for start in range((n - 2) // 2, -1, -1):
        sift_down(arr, start, n - 1)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)

# Start the logger thread.
log_thread = threading.Thread(target=logger, daemon=True)
log_thread.start()

start = time.monotonic()
heapsort(arr)
elapsed = time.monotonic() - start

# Tell the logger to stop and wait for it to flush.
done.set()
log_thread.join()

# Move to a new line so the final print doesn't sit on the ticker.
print()

print(f"n={n} time={elapsed:.3f}s samples={len(samples)}")

# Save samples to a CSV for later analysis.
with open("heap_temps.csv", "w") as f:
    f.write("elapsed_s,temp_c\n")
    for t, T in samples:
        f.write(f"{t:.3f},{T:.3f}\n")
print("Wrote heap_temps.csv")
