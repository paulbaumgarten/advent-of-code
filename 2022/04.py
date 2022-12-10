import time, math
from pprint import pprint

start = time.time()
with open("./2022/day4.txt", "r") as f:
    data = f.read().splitlines()

demo = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

def part1(data):
    fullycontained = 0
    for pair in data:
        print(pair)
        elf1,elf2=pair.split(",")
        e1from, e1stop = elf1.split("-")
        e2from, e2stop = elf2.split("-")
        e1list = [n for n in range(int(e1from),int(e1stop)+1)]
        e2list = [n for n in range(int(e2from),int(e2stop)+1)]
        contained = True
        for n in e1list:
            if n not in e2list:
                contained = False
                break
        if not contained:
            contained = True
            for n in e2list:
                if n not in e1list:
                    contained = False
                    break
        if contained: fullycontained+=1
    print(fullycontained)

def part2(data):
    overlap = 0
    for pair in data:
        print(pair)
        elf1,elf2=pair.split(",")
        e1from, e1stop = elf1.split("-")
        e2from, e2stop = elf2.split("-")
        e1list = [n for n in range(int(e1from),int(e1stop)+1)]
        e2list = [n for n in range(int(e2from),int(e2stop)+1)]
        for n in e1list:
            if n in e2list:
                overlap+=1
                break
    print(overlap)

part1(data)
part2(data)
print("Execution time:",time.time()-start)
