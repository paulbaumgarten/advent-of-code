# --- Day 1: Sonar Sweep ---

with open("01a.data", "r") as f:
    d = f.read().splitlines()

d = [int(v) for v in d]
count = 0
prev = d[0]
for i in range(3, len(d)):
    a = d[i] + d[i-1] + d[i-2]
    b = d[i-1] + d[i-2] + d[i-3]
    if a > b:
        count += 1
print(count)

# 1702