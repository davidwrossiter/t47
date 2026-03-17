# bubble.py
import sys
import time

if len(sys.argv) != 2:
    print("usage: bubble.py <datafile>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as f:
    arr = [int(line) for line in f]

n = len(arr)

start = time.monotonic()

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

elapsed = time.monotonic() - start
print(f"n={n} time={elapsed:.3f}s")
