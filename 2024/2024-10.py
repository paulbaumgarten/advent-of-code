import math, random, numpy, os, re, copy, time

DEMO = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def find_zeros(data):
    results = []
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == 0:
                results.append((y,x))
    return results

def traverse(data, start):
    nines = []
    q = [start]
    while len(q) > 0:
        current = q.pop(0)
        y,x = current
        val = int(data[y][x])
        if val == 9:
            if (y,x) not in nines:
                nines.append((y,x))
                continue
        # Find up, down, left, right that are an increase in value of 1
        if y > 0 and data[y-1][x] == val+1 and (y-1,x) not in q:
            q.append((y-1,x))
        if y < len(data)-1 and data[y+1][x] == val+1 and (y+1,x) not in q:
            q.append((y+1,x))
        if x > 0 and data[y][x-1] == val+1 and (y,x-1) not in q:
            q.append((y,x-1))
        if x < len(data[y])-1 and data[y][x+1] == val+1 and not (y,x+1) in q:
            q.append((y,x+1))        
    return nines

def traverse2(data, start):
    nines = []
    q = [(start, [])]
    while len(q) > 0:
        current, path = q.pop(0)
        y,x = current
        path = path + [current]
        val = int(data[y][x])
        if val == 9:
            nines.append((path))
            continue
        # Find up, down, left, right that are an increase in value of 1
        if y > 0 and data[y-1][x] == val+1 and ((y-1,x),path) not in q:
            q.append( ((y-1,x),path) )
        if y < len(data)-1 and data[y+1][x] == val+1 and ((y+1,x),path) not in q:
            q.append( ((y+1,x),path) )
        if x > 0 and data[y][x-1] == val+1 and ((y,x-1),path) not in q:
            q.append( ((y,x-1),path) )
        if x < len(data[y])-1 and data[y][x+1] == val+1 and not ((y,x+1),path) in q:
            q.append( ((y,x+1),path) )  
    return nines

def part1(raw):
    data = DEMO[:]
    data = raw[:]
    data = [[int(n) for n in line] for line in data]
    zeros = find_zeros(data)
    score = 0
    print("Zeros at ",zeros)
    for i in range(0, len(zeros)):
        print(f"Processing {zeros[i]}")
        nines = traverse(data, zeros[i])
        print(f"   - Found {len(nines)} => {nines}")
        score += len(nines)
    return score

def part2(raw):
    data = DEMO[:]
    data = raw[:]
    data = [[int(n) for n in line] for line in data]
    zeros = find_zeros(data)
    score = 0
    print("Zeros at ",zeros)
    for i in range(0, len(zeros)):
        print(f"Processing {zeros[i]}")
        nines = traverse2(data, zeros[i])
        print(f"   - Found {len(nines)} => {nines}")
        score += len(nines)
    return score

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


