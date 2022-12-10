import time, math
from pprint import pprint

start = time.time()
with open("./2022/day6.txt", "r") as f:
    data = f.read().splitlines()

# Start of packet = 4 chars that are all different

"""
"""

def part1(data):
    for i in range(4,len(data)):
        partial = data[i-4:i]
        header = True
        #print(f"Checking ",partial)
        for p in range(0, 3):
            for q in range(p+1, 4):
                if partial[p] == partial[q]: header = False
        if header:
            return i
    return -1

def part2(data):
    for i in range(14,len(data)):
        partial = data[i-14:i]
        header = True
        #print(f"Checking ",partial)
        for p in range(0, 13):
            for q in range(p+1, 14):
                if partial[p] == partial[q]: header = False
        if header:
            return i
    return -1

print(part1("mjqjpqmgbljsphdztnvjfqwrcgsmlb")) # 7
print(part1("bvwbjplbgvbhsrlpgdmjqwftvncz")) # 5
print(part1("nppdvjthqldpwncqszvftbrmjlhg")) # 6
print(part1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")) # 10
print(part1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")) # 11
print(part1(data[0]))

print(part2("mjqjpqmgbljsphdztnvjfqwrcgsmlb")) # 7
print(part2("bvwbjplbgvbhsrlpgdmjqwftvncz")) # 5
print(part2("nppdvjthqldpwncqszvftbrmjlhg")) # 6
print(part2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")) # 10
print(part2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")) # 11
print(part2(data[0]))
print("Execution time:",time.time()-start)
