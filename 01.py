# --- Day 1: Sonar Sweep ---

with open("01a.data", "r") as f:
    d = f.read().splitlines()

d = [int(v) for v in d]
count = 0
prev = d[0]
for i in range(1, len(d)):
    if d[i] > d[i-1]:
        count += 1
print(count)

# 1665

