import time, math
from pprint import pprint

def part1(data):
    pass

def part2(data):
    pass

start = time.time()

def parse(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    return data

data = parse("./2022/day---.txt")
print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)
