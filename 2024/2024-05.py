import math, random, numpy, os, re

DEMO = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

# 75,97,47,61,53 becomes 97,75,47,61,53.
# 61,13,29 becomes 61,29,13.
# 97,13,75,29,47 becomes 97,75,47,29,13.

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

def part1(raw):
    data = raw[:]
    #data = DEMO[:].splitlines()
    rules = []
    have_rules = set()
    pages = []
    process_rules = True
    middle = []
    incorrects = []
    for i,v in enumerate(data):
        if v == "":
            process_rules = False
        elif process_rules:
            parts = v.split("|")
            rules.append((int(parts[0]), int(parts[1])))
            have_rules.add(int(parts[0]))
            have_rules.add(int(parts[1]))
        else:
            pages.append( [ int(n) for n in v.split(",") ])
    #print("pages",pages)
    for i,pagelist in enumerate(pages):
        print("pagelist",pagelist)
        ok = True
        for x,page in enumerate(pagelist):
            if page in have_rules:
                for y,rule in enumerate(rules):
                    if (page == rule[0]) and (rule[1] in pagelist) and (rule[1] not in pagelist[x:]):
                        ok = False
                        break
                    if (page == rule[1]) and (rule[0] in pagelist) and (rule[0] not in pagelist[:x]):
                        ok = False
                        break
        if ok:
            print(" - ok")
            mid = len(pagelist) // 2
            middle.append(pagelist[mid])
        else:
            print(" - fail")
            incorrects.append(pagelist)
    total = sum(middle)
    return total
# 6461 too high
# 1401 too low
# 5964

def part2(raw):
    data = raw[:]
    #data = DEMO[:].splitlines()
    rules = []
    have_rules = set()
    pages = []
    process_rules = True
    middle = []
    incorrects = []
    for i,v in enumerate(data):
        if v == "":
            process_rules = False
        elif process_rules:
            parts = v.split("|")
            rules.append((int(parts[0]), int(parts[1])))
            have_rules.add(int(parts[0]))
            have_rules.add(int(parts[1]))
        else:
            pages.append( [ int(n) for n in v.split(",") ])
    #print("pages",pages)
    for i,pagelist in enumerate(pages):
        print("pagelist",pagelist)
        ok = True
        for x,page in enumerate(pagelist):
            if page in have_rules:
                for y,rule in enumerate(rules):
                    if (page == rule[0]) and (rule[1] in pagelist) and (rule[1] not in pagelist[x:]):
                        ok = False
                        break
                    if (page == rule[1]) and (rule[0] in pagelist) and (rule[0] not in pagelist[:x]):
                        ok = False
                        break
        if not ok:
            incorrects.append(pagelist)
    # Deal with the incorrects
    corrected = []
    for i, fix in enumerate(incorrects):
        print("Processing",fix)
        swapped = True
        while swapped:
            swapped = False
            # Check the before pairs
            for p in range(len(fix)-1):
                for q in range(p+1, len(fix)):
                    if (fix[q],fix[p]) in rules:
                        print("      swapping ",(fix[q],fix[p])," at ",(p,q))
                        fix[p], fix[q] = fix[q], fix[p]
                        swapped = True
        corrected.append(fix)
        print("  now     ",fix)
    for c in corrected:
        mid = len(c) // 2
        middle.append(c[mid])
    total = sum(middle)
    return total # 4719

if __name__=="__main__":
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)


