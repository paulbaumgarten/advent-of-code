from pprint import pprint

with open("./2022/day1.txt", "r") as f:
    data = f.read().splitlines()

elf_totals = []

def part1():
    # Find calories per Elf
    this_elf = 0
    for x in range(0, len(data)):
        if data[x] != "":
            this_elf += int(data[x])
        else:
            elf_totals.append(this_elf)
            this_elf = 0
    # Find Elf with most calories
    most = max(elf_totals)
    print(f"Winner Elf { elf_totals.index(most) + 1 } has { most }")

def part2():
    # Find Elfs with top 3 calories
    elf_sorted = sorted(elf_totals)
    print(sum(elf_sorted[-3:]))

part1() # Winner Elf 29 has 71300
part2() # 209691

