import math, random, numpy, os, re

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

def part1(raw):
    data = " ".join(raw)
    query = r'mul\(\d+,\d+\)'
    possibles = re.findall(query,data)
    total = 0
    for calc in possibles:
        #print(calc)
        comma = calc.find(",")
        n1 = calc[4:comma]
        n2 = calc[comma+1:-1]
        total = total + int(n1) * int(n2)
    return total
    
# 27623467
# 27851208 too low
# 178211538 too low
# 1075525869 not correct
# 178794710 correct

def part2(raw):
    total = 0
    enabled = True
    data = " ".join(raw)
    reg = re.compile(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))")
    for match in reg.finditer(data):
        #print(match)
        if match.group() == "do()":
            enabled = True
        elif match.group() == "don't()":
            enabled = False
        elif enabled:
            calc = match.group()
            comma = calc.find(",")
            n1 = calc[4:comma]
            n2 = calc[comma+1:-1]
            total = total + int(n1) * int(n2)
    return total
# part 2
# 76729637

if __name__=="__main__":
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)


