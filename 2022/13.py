import time, math
from pprint import pprint

def compare1(left, right):
    if left[0]=="[" and left[-1]=="]":
        left = left[1:-1]
    if right[0]=="[" and right[-1]=="]":
        right = right[1:-1]
    

def part1(data):
    indicies = 0
    for i in range(len(data)):
        if compare1(data[i]["left"], data[i]["right"]):
            print(f"Pair {i+1} left wins")
            indicies += i+1
        else:
            print(f"Pair {i+1} right wins")
    return indicies


def part2(data):
    pass

start = time.time()

def parse(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    res = []
    for i in range(0, len(data),3):
        res.append({"left": data[i], "right": data[i+1]})
    return res

data = parse("./2022/day13a.txt")
print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)
