import time, math
from pprint import pprint
import copy

def part1(data):
    moved = copy.copy(data)
    # Encrypt
    for n in range(0, len(data)):
        val = data[n]
        pos = moved.index(val)
        new_pos = val+pos
        while new_pos < 0:
            new_pos = new_pos + len(data)
        print(f"Moving {val} from {pos} to {new_pos}")
        if new_pos > pos:
            while new_pos > pos:
                tmp = moved[pos]
                moved[pos] = moved[pos+1]
                moved[pos+1] = tmp
                pos += 1
        elif new_pos > pos:
            while new_pos < pos:
                tmp = moved[pos]
                moved[pos] = moved[pos-1]
                moved[pos-1] = tmp
                pos -= 1
        print(moved)
    onethou = moved[ 1001 % len(moved) ]
    twothou = moved[ 2001 % len(moved) ]
    threethou = moved[ 3001 % len(moved) ]
    print(moved,onethou,twothou,threethou)
    result = onethou + twothou + threethou
    return result

def part2(data):
    pass

def parse(filename):
    with open(filename, "r") as f:
        data = [int(n) for n in f.read().splitlines()]
    return data

start = time.time()
data = parse("./2022/day 20 example.txt")
print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)

