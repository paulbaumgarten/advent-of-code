import time, math
from pprint import pprint

start = time.time()
with open("./2022/day11b.txt", "r") as f:
    data = f.read().splitlines()

def parse(data):
    monkeys = {}
    monkey = 0
    for line in data:
        if line.startswith("Monkey "):
            monkey = int(line[7:-1])
            monkeys[monkey] = {}
            monkeys[monkey]["inspected"] = 0
            print(f"Parsing monkey {monkey}")
        if line.startswith("  Starting items: "):
            monkeys[monkey]["items"] = [int(n) for n in line[18:].split(", ")]
        if line.startswith("  Operation: new = "):
            monkeys[monkey]["operation"] = line[19:].split(" ")
        if line.startswith("  Test: divisible by "):
            monkeys[monkey]["test"] = int(line[21:])
        if line.startswith("    If true: throw to monkey "):
            monkeys[monkey]["true"] = int(line[29:])
        if line.startswith("    If false: throw to monkey "):
            monkeys[monkey]["false"] = int(line[30:])
    pprint(monkeys)
    return monkeys

def part1(monkeys):
    for round in range(1,21):
        print(f"Round {round}")
        for id,monkey in monkeys.items(): # Every monkey
            for i in range(len(monkey["items"])): # Every item the monkey has
                print(f"Monkey {id} item #{i} value { monkeys[id]['items'][i] }")
                worry = monkeys[id]["items"][i]
                # Perform worry operation
                opcode = monkeys[id]["operation"][1]
                operand = monkeys[id]["operation"][2]
                if operand == "old":
                    operand = worry
                else:
                    operand = int(operand)
                if opcode == "+":
                    worry = worry + operand
                elif opcode == "*":
                    worry = worry * operand
                # Monkey boredom
                worry = worry // 3
                # Test and throw
                print(f"  - Testing { worry }")
                if worry % monkeys[id]["test"] == 0:
                    throw_to = monkeys[id]["true"]
                else:
                    throw_to = monkeys[id]["false"]
                monkeys[throw_to]["items"].append(worry)
                # Log the inspection
                monkeys[id]["inspected"] += 1
            # All items thrown, reset items list
            monkeys[id]["items"] = []
    # Calculate monkey business value
    inspections = []
    for k in monkeys.keys():
        inspections.append(monkeys[k]["inspected"])
    inspections = sorted(inspections)
    print(inspections[-2] * inspections[-1])
    return monkeys

def part2(monkeys, reducer):
    for round in range(1,10001):
        print(f"Round {round}")
        for id,monkey in monkeys.items(): # Every monkey
            for i in range(len(monkey["items"])): # Every item the monkey has
                print(f"Monkey {id} item #{i} value { monkeys[id]['items'][i] }")
                worry = monkeys[id]["items"][i]
                # Perform worry operation
                opcode = monkeys[id]["operation"][1]
                operand = monkeys[id]["operation"][2]
                if operand == "old":
                    operand = worry
                else:
                    operand = int(operand)
                if opcode == "+":
                    worry = worry + operand
                elif opcode == "*":
                    worry = worry * operand
                # Monkey boredom
                # worry = worry // 3
                # Test and throw
                print(f"  - Testing { worry }")
                if worry % monkeys[id]["test"] == 0:
                    throw_to = monkeys[id]["true"]
                else:
                    throw_to = monkeys[id]["false"]
                monkeys[throw_to]["items"].append(worry % reducer)
                # Log the inspection
                monkeys[id]["inspected"] += 1
            # All items thrown, reset items list
            monkeys[id]["items"] = []
    # Calculate monkey business value
    inspections = []
    for k in monkeys.keys():
        inspections.append(monkeys[k]["inspected"])
    inspections = sorted(inspections)
    print(inspections)
    print(inspections[-2] * inspections[-1])

monkeys = parse(data)
#pprint(part1(monkeys))

reducer = 7*11*13*3*17*2*5*19 # Real data
# reducer = 23*19*13*17 # Sample data
print(part2(monkeys, reducer))
print("Execution time:",time.time()-start)
