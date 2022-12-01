from pprint import pprint

with open("./2022/day1.txt", "r") as f:
    data = f.read().splitlines()
elf_totals = []

def part1():
    elf = []
    for x in range(0, len(data)):
        if data[x] != "":
            elf.append(int(data[x]))
        else:
            elf_totals.append(sum(elf))
            elf = []
    x = 0
    for i in range(0, len(elf_totals)):
        print(f"Elf {i+1} has {elf_totals[i]}")
        if elf_totals[i] > elf_totals[x]:
            x = i
    print(f"Winner Elf {x+1} has {elf_totals[x]}")

def part2():
    elf_sorted = sorted(elf_totals)
    print(elf_sorted)    
    print(sum(elf_sorted[-3:]))

part1()
part2()

