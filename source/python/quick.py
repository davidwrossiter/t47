# quick.py

import sys
import time

sys.setrecursionlimit(1_000_000)

if len(sys.argv) != 2:
    print("usage: quick.py <datafile>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as f:
    arr = [int(line) for line in f]

n = len(arr)

def quicksort(arr, lo, hi):
    if lo < hi:
        # Lomuto partition with last element as pivot.
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

start = time.monotonic()
quicksort(arr, 0, n - 1)
elapsed = time.monotonic() - start
print(f"n={n} time={elapsed:.3f}s")
