import time, math
from pprint import pprint
from copy import deepcopy

def compare1(left, right):
    #print(f"Comparing {left} {right}")
    i = 0
    while i < len(left) and i < len(right):
        if type(left[i])==list and type(right[i])==list:
            res = compare1(left[i], right[i])
            if res=="left" or res=="right":
                return res
        if type(left[i])==int and type(right[i])==int:
            if left[i]<right[i]: return "left"
            if left[i]>right[i]: return "right"
        if type(left[i])==list and type(right[i])==int:
            res = compare1(left[i], [right[i]])
            if res=="left" or res=="right":
                return res
        if type(left[i])==int and type(right[i])==list:
            res = compare1([left[i]], right[i])
            if res=="left" or res=="right":
                return res
        i+=1
    if len(left) < len(right):
        return "left"
    if len(left) > len(right):
        return "right"
    #print(f"Neither left {left} right {right}")
    return "neither"

def part1(data):
    print("")
    indicies = 0
    for i in range(len(data)):
        if compare1(data[i]["left"], data[i]["right"]) == "left":
            #print(f"Pair {i+1} left wins")
            indicies += i+1
        else:
            #print(f"Pair {i+1} right wins")
            pass
    return indicies

def part2(data):
    # Bubble sort? Why not... it is tradition after all
    print("\nSorting...")
    swap = True
    while swap:
        swap = False
        for i in range(0, len(data)-1):
            if compare1(data[i], data[i+1]) == "right":
                #print("Swapping ",data[i],"and",data[i+1])
                tmp = deepcopy(data[i])
                data[i] = deepcopy(data[i+1])
                data[i+1] = deepcopy(tmp)
                swap = True
    two = 0
    six = 0
    for i in range(0,len(data)):
        if data[i] == [[2]]: two=i+1
        if data[i] == [[6]]: six=i+1
    return two*six

start = time.time()

def parse_into_lists(s,depth=0):
    #print(f"{depth} parse_into_lists: {s}")
    tokens = []
    if s[0] == "[": s=s[1:]
    while len(s)>0:
        if s[0] == "[":
            brackets = 1
            close = 1
            while brackets > 0:
                if s[close] == "[":
                    brackets += 1
                if s[close] == "]":
                    brackets -= 1
                close += 1
            tokens.append(parse_into_lists(s[0:close], depth+1))
            s = s[close:]
        elif s[0] == ",":
            s = s[1:]
        elif s[0].isnumeric():
            until = 0
            while s[until].isnumeric():
                until += 1
            tokens.append(int(s[0:until]))
            s = s[until:]
        elif s[0] == "]":
            #print(f"retuning {tokens}")
            return tokens
    #print(f"retuning {tokens}")
    return tokens[0]

def parse1(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    res = []
    for i in range(0, len(data),3):
        res.append({"left": parse_into_lists(data[i]), "right": parse_into_lists(data[i+1])})
    return res

def parse2(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    res = []
    for i in range(0, len(data),3):
        res.append(parse_into_lists(data[i]))
        res.append(parse_into_lists(data[i+1]))
    res.append(parse_into_lists("[[2]]"))
    res.append(parse_into_lists("[[6]]"))
    return res

data = parse1("./2022/day13b.txt")
print(part1(data))

data = parse2("./2022/day13b.txt")
print(part2(data))

print("Execution time:",time.time()-start)
