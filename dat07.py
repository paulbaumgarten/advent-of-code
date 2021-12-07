
# Prepare data
with open("day07.txt", "r") as f:
    data = f.read().splitlines()
data = data[0].split(",")
data = [int(d) for d in data]
# Sort and find the median
data.sort()
median = data[len(data) // 2]
# Calculate fuel for part 1
fuel = 0
for n in data:
    diff = abs(n-median)
    print("adding ",n,"diff",diff)
    fuel += diff
print(fuel)

def triangular(n):
    return n * (n+1) / 2

results = []
lowestfuel = 999999999999
lowestfueli = 0
for objective in range(0,1899):
    fueltotal=0
    for n in data:
        fuelindividual = triangular(abs(n-objective)) # 1 +2 +3 +4 +5 ,,, 1 3 6 10 15
        fueltotal += fuelindividual
        # print("For element",n,"fuel",fuelindividual)
    print(objective,fueltotal)
    if fueltotal < lowestfuel:
        lowestfuel = fueltotal
        lowestfueli = objective
    results.append((objective,fueltotal))
print("optimal position",lowestfueli, "requires lowest fuel",lowestfuel)

