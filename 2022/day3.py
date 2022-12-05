import time
from pprint import pprint

start = time.time()
with open("./2022/day3.txt", "r") as f:
    data = f.read().splitlines()

demo = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

"""
priority:
 - a through z have priorities 1 through 26.
 - A through Z have priorities 27 through 52.
"""

def part1(data):
    score = 0
    for x in range(0,len(data)):
        rucksack = data[x]
        part1 = rucksack[0:len(rucksack)//2]
        part2 = rucksack[len(rucksack)//2:]
        print(x,part1,part2,end=" ")
        for y in range(0, len(part1)):
            letter = part1[y]
            if letter in part2:
                print(f"found {letter}")
                if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    score += ord(letter)-ord('A')+1+26
                else:
                    score += ord(letter)-ord('a')+1
                break
    return score

def part2(data):
    score = 0
    for x in range(0,len(data),3):
        print(f"Rucksacks {x} to {x+2}.",end=" ")
        # Find the one letter in common between data[x], data[x+1] and data[x+2]
        for letter in data[x]:
            if letter in data[x+1] and letter in data[x+2]:
                print(f"found letter {letter}")
                if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    score += ord(letter)-ord('A')+1+26
                else:
                    score += ord(letter)-ord('a')+1
                break
    return score

print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)
