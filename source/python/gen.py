# gen.py
import random, sys
n = int(sys.argv[1])
random.seed(42)
with open("data.txt", "w") as f:
    for _ in range(n):
        f.write(f"{random.randint(0, 10**9)}\n")
