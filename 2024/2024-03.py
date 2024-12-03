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
    sequence = "ul(.,.)"
    query = "m.?u.?l.?\(.?[0-9]*.?,[0-9]*.?\)"
    query = "m.*?u.*?l.*?\(.*?[0-9]*?.*?,[0-9]*?.*?\)"
    """
    possibles = re.findall(query,data)
    #print("\n".join(possibles))
    total = 0
    for calc in possibles:
        print(calc)
        calc = calc[ calc.rfind("(")+1 : ]
        calc = calc[ : calc.find(")") ]        
        vals = calc.split(",")
        print("   ",vals)
        n1 = ""
        n2 = ""
        for ch in vals[0]:
            if ch.isnumeric():
                n1 = n1+ch
        for ch in vals[1]:
            if ch.isnumeric():
                n2 = n2+ch
        total = total + int(n1) * int(n2)
    return total
    #print("\n".join(possibles))
    """
    possibles = data.split("mul(")
    total = 0
    for i in range(len(possibles)):
        pos = 0
        n1 = 0
        n2 = 0
        first = True
        item = possibles[i]
        print(item)
        if "," not in item:
            continue
        comma = item.find(",")
        n1 = item[:comma]
        if not n1.isnumeric():
            continue
        item = item[comma+1:]
        if ")" not in item:
            continue
        closing = item.find(")")
        n2 = item[:closing]
        if not n2.isnumeric():
            continue
        print("   ",n1,"*",n2)
        total = total + int(n1) * int(n2)

    """
    for i in range(len(possibles)):
        pos = 0
        n1 = 0
        n2 = 0
        first = True
        item = possibles[i]
        print(item)
        for ch in item:
            if pos >= len(sequence):
                break
            if ch == sequence[pos] and ch != ".":
                pos += 1
            elif ch in "0123456789" and sequence[pos] == ".":
                if first:
                    n1 = n1*10 + int(ch)
                else:
                    n2 = n2*10 + int(ch)
            elif ch == "," and sequence[pos] == ".":
                pos += 2
                first = False
            elif ch == ")" and sequence[pos] == ".":
                pos += 2
                print("   ",n1,"*",n2)
                total = total + n1*n2
                break
    """
    return total
# 27623467
# 27851208 too low
# 178211538 too low
# 1075525869 not correct
# 178794710 correct

def part2(raw):
    enabled = True
    data = " ".join(raw)
    mul = data.find("mul(")
    do = data.find("do()")
    dont = data.find("don't()")
    total = 0
    while mul >= 0:
        if do >= 0 and dont >= 0 and (do < mul or dont < mul):
            if do < mul < dont:
                enabled = True
            elif do < dont < mul:
                enabled = False
            elif dont < do < mul:
                enabled = True
            elif dont < mul < do:
                enabled = False
        elif do >= 0 and do < mul and dont < 0:
            enabled = True
        elif dont >= 0 and dont < mul and do < 0:
            enabled = False
        print(data[mul:mul+20],"     ",mul)
        closing = data[mul+4:].find(")")
        item = data[mul+4:mul+closing+5]
        n1 = 0
        n2 = 0
        print("  item:",item)
        if "," in item:
            comma = item.find(",")
            n1 = item[:comma]
            if n1.isnumeric():
                item = item[comma+1:]
                if ")" in item:
                    closing = item.find(")")
                    n2 = item[:closing]
                    if n2.isnumeric():
                        if enabled:
                            print("   ",n1,"*",n2)
                            total = total + int(n1) * int(n2)
                        else:
                            print("   ",n1,"*",n2,"   DISABLED")
        data = data[mul+4:]
        do = data.find("do()")
        dont = data.find("don't()")
        mul = data.find("mul(")        
    return total
# part 2
# 76729637

if __name__=="__main__":
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)


