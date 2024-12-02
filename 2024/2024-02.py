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
    safe = 0
    for test in data:
        ok = True
        test = test.split(" ")
        test = [int(n) for n in test]
        last_diff = test[1]-test[0]
        for i in range(1, len(test)):
            diff = test[i]-test[i-1]
            if (diff > -1 and diff < 1) or diff > 3 or diff < -3:
                ok = False
            if (last_diff > 0 and diff < 0) or (last_diff < 0 and diff > 0):
                ok = False
        if ok:
            safe += 1
    return safe # 359

def part2(data):
    safe = 0
    for test in data:
        unsafe = 0
        test = test.split(" ")
        test = [int(n) for n in test]
        last_diff = test[1]-test[0]
        for i in range(1, len(test)):
            diff = test[i]-test[i-1]
            if (diff > -1 and diff < 1) or diff > 3 or diff < -3:
                unsafe += 1
            if (last_diff > 0 and diff < 0) or (last_diff < 0 and diff > 0):
                unsafe += 1
            last_diff = diff
        if unsafe <= 1:
            safe += 1
    return safe
    # 418

if __name__=="__main__":
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)


