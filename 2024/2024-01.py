import math, random, numpy, os

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

def part1(data):
    a = []
    b = []
    delta = []
    for item in data:
        p,q = item.split("   ")
        a.append(int(p))
        b.append(int(q))
    a.sort()
    b.sort()
    for i in range(len(a)):
        delta.append( abs(a[i]-b[i] ))
    return(sum(delta))    

def part2(data):
    a = []
    b = []
    delta = []
    for item in data:
        p,q = item.split("   ")
        a.append(int(p))
        b.append(int(q))
    similarity = 0
    for i in range(len(a)):
        similarity += a[i] * b.count(a[i])
    return similarity

if __name__=="__main__":
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)


