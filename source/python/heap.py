# heap.py

import sys
import time

if len(sys.argv) != 2:
    print("usage: heap.py <datafile>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as f:
    arr = [int(line) for line in f]

n = len(arr)

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
    # Build the heap.
    for start in range((n - 2) // 2, -1, -1):
        sift_down(arr, start, n - 1)
    # Repeatedly extract the maximum.
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)

start = time.monotonic()
heapsort(arr)
elapsed = time.monotonic() - start
print(f"n={n} time={elapsed:.3f}s")
