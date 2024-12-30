import math, random, numpy, os, re, copy, time

EX="""r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def is_possible(patterns, design):
    #print("  design",design)
    if design == "": return True
    if design in patterns: return True
    for i in range(0, len(design)):
        if design[0:i] in patterns:
            #print("    found",design[0:i])
            sub_ok = is_possible(patterns, design[i:])
            if sub_ok:
                return True
    return False

def part1(raw):
    data = EX[:]
    data = raw[:]
    patterns = data[0].split(", ")
    designs = data[2:]
    possible = 0
    print(f"patterns: {len(patterns)}")
    print(f"designs : {len(designs)}")
    for i in range(0, len(designs)):
        print(f"Design {i} {designs[i]}...",end="")
        if is_possible(patterns, designs[i]):
            possible += 1
            print("possible")
        else:
            print("not possible")
    return possible

def part2(raw):
    pass

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


