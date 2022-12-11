import time, math
from pprint import pprint

start = time.time()
with open("./2022/day10b.txt", "r") as f:
    data = f.read().splitlines()

def part1(data):
    x = 1
    cycle = 1
    points = [20,60,100,140,180,220]
    signals = []
    for i in range(0, len(data)):
        if data[i][0:4] == "noop":
            if cycle in points:
                signals.append(x)
            cycle +=1
        if data[i][0:4] == "addx":
            if cycle in points:
                signals.append(x)
            if cycle+1 in points:
                signals.append(x)
            cycle +=2
            v = int(data[i][5:])
            x += v
    print(signals)
    result = 0
    for i in range(0, len(signals)):
        result += points[i] * signals[i]
    return result

def part2(data):
    x = 1
    pc = 0 # Program counter
    next_instr_delay = 0
    print("X",end="")
    for cycle in range(1,241):
        # Start of cycle
        if (cycle % 40) in [x-1, x, x+1]:
            print("X",end="")
        else:
            print(".",end="")
        if cycle % 40 == 39:
            print() # Next row
        # Read the instruction
        if next_instr_delay == 0:
            cir = data[pc][0:4]
            if cir == "addx":
                v = int(data[pc][5:])
                x += v
                next_instr_delay = 2
            if cir == "noop":
                next_instr_delay = 1
            pc +=1
        # End of cycle
        next_instr_delay -= 1

print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)
