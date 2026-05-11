# merge_iter.py
# Iterative bottom-up merge sort, avoids recursion limit issues.

import sys
import time

if len(sys.argv) != 2:
    print("usage: merge_iter.py <datafile>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as f:
    arr = [int(line) for line in f]

n = len(arr)

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

start = time.monotonic()
merge_sort(arr)
elapsed = time.monotonic() - start
print(f"n={n} time={elapsed:.3f}s")
