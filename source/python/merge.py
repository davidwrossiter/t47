# merge.py
import sys
import time

if len(sys.argv) != 2:
    print("usage: merge.py <datafile>", file=sys.stderr)
    sys.exit(1)

with open(sys.argv[1]) as f:
    arr = [int(line) for line in f]

n = len(arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

start = time.monotonic()
arr = merge_sort(arr)
elapsed = time.monotonic() - start
print(f"n={n} time={elapsed:.3f}s")
