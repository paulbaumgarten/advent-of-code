
with open("02a.txt", "r") as f:
    data = f.read().splitlines()

horiz = 0
depth = 0
aim = 0
for instr in data:
    direction, amount = instr.split(" ")
    amount = int(amount)
    if direction == "forward":
        horiz += amount
        depth += (aim * amount)
    elif direction == "down":
        #depth += amount
        aim += amount
    elif direction == "up":
        #depth -= amount
        aim -= amount

print(horiz, depth)
print(horiz * depth)
# 2044620088
