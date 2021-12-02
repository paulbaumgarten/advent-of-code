
with open("02a.txt", "r") as f:
    data = f.read().splitlines()

horiz = 0
depth = 0
for instr in data:
    direction, amount = instr.split(" ")
    amount = int(amount)
    if direction == "forward":
        horiz += amount
    elif direction == "down":
        depth += amount
    elif direction == "up":
        depth -= amount

print(horiz, depth)
print(horiz * depth)

# 2147104