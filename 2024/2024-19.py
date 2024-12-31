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

def is_possible1(patterns, design):
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

def is_possible(patterns, design):
    timer = time.time()
    match_at = {}
    for i in range(0, len(design)):
        match_at[i] = []
    if design == "": return True
    if design in patterns: return True
    max_pattern_len = 0
    for i in range(0, len(patterns)):
        if len(patterns[i]) > max_pattern_len:
            max_pattern_len = len(patterns[i])
        for j in range(0, len(design)):
            if design[j:j+len(patterns[i])] == patterns[i]:
                if len(patterns[i]) not in match_at[j]:
                    match_at[j].append(len(patterns[i]))
    #print(match_at)
    reachable = [0]
    start_from = 0
    for x in range(len(design)):
        for val in reachable:
            can_go_to_list = match_at[val]
            for can_go_to in can_go_to_list:
                if val+can_go_to not in reachable:
                    reachable.append(val+can_go_to)
                    if val+can_go_to == len(design):
                        return True
        #print(x,"=>",reachable)
    return False

def count_solutions(patterns, design):
    timer = time.time()
    match_at = {}
    for i in range(0, len(design)):
        match_at[i] = []
    if design == "": return True
    if design in patterns: return True
    max_pattern_len = 0
    for i in range(0, len(patterns)):
        if len(patterns[i]) > max_pattern_len:
            max_pattern_len = len(patterns[i])
        for j in range(0, len(design)):
            if design[j:j+len(patterns[i])] == patterns[i]:
                match_at[j].append(len(patterns[i]))
    #print(match_at)
    solutions = [0] * (len(design)+1)
    solutions[0] = 1
    for i in range(len(design)):
        #print(solutions)
        for j in range(len(match_at[i])):
            val = match_at[i][j]
            solutions[i+val] += solutions[i]
    #print(solutions)
    return solutions[-1]

def part1(raw):
    data = EX[:]
    data = raw[:]
    patterns = data[0].split(", ")
    designs = data[2:]
    possible = 0
    possible_designs = []
    print(f"patterns: {len(patterns)}")
    print(f"designs : {len(designs)}")
    for i in range(0, len(designs)):
        print(f"Design {i} {designs[i]}...",end="")
        if is_possible(patterns, designs[i]):
            possible += 1
            print("possible")
            possible_designs.append(designs[i])
        else:
            print("not possible")
    return possible, possible_designs, patterns

def part2(raw, designs, patterns):
    print(f"patterns: {len(patterns)}")
    print(f"designs : {len(designs)}")
    total = 0
    for i in range(0, len(designs)):
        print(f"Design {i} {designs[i]}...",end="")
        solutions = count_solutions(patterns, designs[i])
        print(solutions)
        total += solutions
    return(total)

if __name__=="__main__":
    start = time.time()
    result, possible_designs, patterns = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data(), possible_designs, patterns)
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


