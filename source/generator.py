import random

n = 50000
data = list(range(n))
random.shuffle(data)

with open("data/50000.txt", "w") as f:
    for x in data:
        f.write(f"{x}\n")
