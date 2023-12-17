import functools
import time
from pprint import pprint
import json
import copy

T = time.time()

FILE = "./2023/2023-12.txt"

TEST = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines() 
# part a 21
# part b 525152

TEST2 = """??.?? 1,1
??.??.??.?? 1,1,1,1
??.??#??.?? 1,1,1,1
??.?????.?? 1,1,1,1""".splitlines()

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    total = 0
    for r in range(0, len(data)):
        pattern, counts = data[r].split(" ")
        counts = [int(n) for n in counts.split(",")]
        print(pattern, counts)
        arrangements_this_pattern = 0
        unknowns = pattern.count("?")
        for i in range(0, 2**unknowns):
            n = i
            this_arrangement = pattern
            while this_arrangement.count("?") > 0:
                new_char = "#" if n % 2 == 0 else "."
                n = n // 2
                this_arrangement = this_arrangement.replace("?", new_char, 1)
            target = ""
            for k in range(0, len(counts)):
                target += "#"*counts[k]
                if k < len(counts)-1:
                    target += "."
            # Does this arrangement match the target
            while this_arrangement.count("..") > 0:
                this_arrangement = this_arrangement.replace("..",".")
            if this_arrangement.startswith("."):
                this_arrangement = this_arrangement[1:]
            if this_arrangement.endswith("."):
                this_arrangement = this_arrangement[:-1]
            #print(this_arrangement, target)
            if this_arrangement == target:
                #print(" -> ",this_arrangement, counts)
                total += 1
    print(total)

def count_patterns_match_target(pattern, target):
    original = pattern
    arrangements_this_pattern = 0
    unknowns = pattern.count("?")
    matches = 0
    for i in range(0, 2**unknowns):
        n = i
        this_arrangement = pattern
        while this_arrangement.count("?") > 0:
            new_char = "#" if n % 2 == 0 else "."
            n = n // 2
            this_arrangement = this_arrangement.replace("?", new_char, 1)
        while this_arrangement.count("..") > 0:
            this_arrangement = this_arrangement.replace("..",".")
        if this_arrangement.startswith("."):
            this_arrangement = this_arrangement[1:]
        if this_arrangement.endswith("."):
            this_arrangement = this_arrangement[:-1]
        if this_arrangement == target:
            matches += 1
    return matches

def is_pattern_partial_match(partial, goal):
    while partial.count("..") > 0:
        partial = partial.replace("..",".")
    if partial.startswith("."):
        partial = partial[1:]
    if partial.endswith("."):
        partial = partial[:-1]
    #print(partial, goal[0:len(partial)])
    return partial == goal[0:len(partial)]

def is_pattern_full_match(partial, goal):
    while partial.count("..") > 0:
        partial = partial.replace("..",".")
    if partial.startswith("."):
        partial = partial[1:]
    if partial.endswith("."):
        partial = partial[:-1]
    #print(partial, goal[0:len(partial)])
    return partial == goal

def pattern_counts(pattern, goal):
    # List of partial matches found so far
    matching = [""]
    full_matches = 0
    while len(matching) > 0:
        match = matching.pop()
        if len(match) == len(pattern):
            if is_pattern_full_match(match, goal):
                #print("          ",match,goal)
                full_matches += 1
        else:
            next_char = pattern[len(match)]
            if next_char == "#":
                if is_pattern_partial_match(match+"#", goal):
                    matching.append(match+"#")
            if next_char == ".":
                if is_pattern_partial_match(match+".", goal):
                    matching.append(match+".")
            if next_char == "?":
                if is_pattern_partial_match(match+"#", goal):
                    matching.append(match+"#")
                if is_pattern_partial_match(match+".", goal):
                    matching.append(match+".")
    return full_matches


NO_FIT = {} # {token_idx { position: True }}
FIT = [] # tuples of (token_idx, position)
CACHE = {} # Depth, start_from
MEMO = []

def find_tokens_this_depth(pattern, counts, depth, start_from=0):
    global NO_FIT, CACHE
    # Memoization - recall
    if depth in CACHE.keys():
        if start_from in CACHE[depth].keys():
            return CACHE[depth][start_from] 
    matches = {}
    current_token_idx = depth
    previous_mandatory_blocks = 0
    mandatory_block_started = False
    prev_ch = '.'
    for i in range(0, start_from):
        ch = pattern[i]
        # Mandatory blocks
        if ch == "#":
            mandatory_block_started = True
        if ch == "." and mandatory_block_started:
            mandatory_block_started = False
            previous_mandatory_blocks += 1
        prev_ch = ch
    for i in range(start_from, len(pattern)):
        ch = pattern[i]
        # Mandatory blocks
        if ch == "#":
            mandatory_block_started = True
        if ch == "." and mandatory_block_started:
            mandatory_block_started = False
            previous_mandatory_blocks += 1
        if (prev_ch in ['.', '?']) and (ch in ['#','?']):
            # Possible start of a block... does it fit?
            fit = True
            if fit and previous_mandatory_blocks > current_token_idx:
                fit = False
            if fit and len(pattern) < (i+counts[current_token_idx]):
                fit = False
            if fit:
                for j in range(0, counts[current_token_idx]):
                    if pattern[i+j] not in ["#", "?"]:
                        fit = False
            if fit:
                if len(pattern) > (i+counts[current_token_idx]) and pattern[i+counts[current_token_idx]] not in ['.','?']:
                    fit = False 
            # Start a new block possible block
            if fit:
                if i not in matches.keys():
                    if current_token_idx==len(counts)-1: # All tokens satisfied
                        # Make sure there aren't left over mandatory blocks before we are ok
                        if pattern[i+counts[current_token_idx]:].count("#") == 0:
                            matches[i]=1
                        else:
                            matches[i]=0
                    elif i+counts[current_token_idx]+1 > len(pattern):
                        fit = False
                        matches[i]=0
                    else:
                        if depth+1 in CACHE.keys() and i+counts[current_token_idx]+1 in CACHE[depth+1].keys():
                            matches[i] = CACHE[depth+1][i+counts[current_token_idx]+1] 
                        else:
                            matches[i] = find_tokens_this_depth(pattern, counts, depth+1, i+counts[current_token_idx]+1)
        prev_ch = ch
    # Memoization - save
    if depth not in CACHE.keys():
        CACHE[depth] = {}
    CACHE[depth][start_from] = copy.deepcopy(matches)
    return matches
# 506250 or 826550 ?

def count_permutations(p):
    #print("layer")
    tot = 0
    for k,v in p.items():
        #print(type(v),v)
        if type(v) == dict:
            tot += count_permutations(v)
        if type(v) == int:
            tot += v
    return tot

def pattern_counts_5(pattern, counts):
    global CACHE, NO_FIT
    CACHE = {}
    NO_FIT = []
    permutations = find_tokens_this_depth(pattern, counts, 0)
    text = json.dumps(permutations,indent=3)
    #print(text)
    full_matches = count_permutations(permutations)
    return full_matches

def counts_to_goal(counts):
    # Convert a counts 1,1,3 into a target string of #.#.###
    goal = ""
    for i in range(0, len(counts)):
        goal += "#"*counts[i]+"."
    goal = goal[:-1]
    return goal

def get_placements(starts, counts, idx, min_start=0):
    place = {}
    for i in range(0, len(starts[idx])):
        if starts[idx][i] >= min_start:
            if idx == len(counts)-1:
                place[ starts[idx][i] ] = 1
            else:
                place[ starts[idx][i] ] = get_placements(starts, counts, idx+1, starts[idx][i]+counts[idx]+1)
    return place

def pattern_counts_6(pattern, counts):
    # 0123456789-1234
    # ???.###

    # 0123456789-123456
    # ???.?###????.?###
    #print("pattern",pattern)
    optional = { n:[] for n in range(0, len(pattern)) }
    mandatory = {}
    mixed = { n:[] for n in range(0, len(pattern)) }

    # Find all the mandatory and optional blocks
    for i in range(0, len(pattern)):
        # Start a block
        ch = pattern[i]
        if i>0:
            prev = pattern[i-1]
        else:
            prev = '.'
        if (ch == "#") and (prev=="?" or prev=="."):
            for j in range(i, len(pattern)):
                if (pattern[j] != "#"):
                    mandatory[i] = j-i
                    break
            if i not in mandatory.keys():
                mandatory[i] = len(pattern)-i
        if (ch == "?") and (prev=="?" or prev=="."):
            for j in range(i, len(pattern)):
                if (pattern[j] == "?"):
                    if j<len(pattern)-1 and pattern[j+1] != "#":
                        optional[i].append(j-i+1)
                    elif j==len(pattern)-1:
                        optional[i].append(j-i+1)
                if pattern[j] != "?":
                    break
    
    # Find all the mixed blocks
    for i in mandatory.keys():
        # Go backwaards as far as possible (looking for optional+mandatory)
        if i > 0 and mandatory[i] != 0:
            for j in range(i-1, -1, -1):
                if pattern[j] == ".":
                    break
                if pattern[j] == "?":
                    #print("i",i,"mandatory[i]",mandatory[i],"j",j)
                    mixed[j].append( mandatory[i]+i-j )
                    # Go forwards as far as possible from the start of the optional+mandatory block (looking for optional+mandatory+optional)
                    if i < len(pattern)-1:
                        for k in range(i+mandatory[i], len(pattern)):
                            if pattern[k] == ".":
                                break
                            if pattern[k] == "?":
                                #print("i",i,"mandatory[i]",mandatory[i],"j",j)
                                mixed[j].append( 1-i+k+1 )
        # Go forwards as far as possible from the start of the mandatory block (looking for mandatory+optional)
        if i < len(pattern)-1:
            for j in range(i+1, len(pattern)):
                if pattern[j] == ".":
                    break
                if pattern[j] == "?" or pattern[j] == "#":
                    #print("i",i,"mandatory[i]",mandatory[i],"j",j)
                    mixed[i].append( 1-i+j )
    #print("mandatory",mandatory)
    #print("optional",optional)
    #print("mixed",mixed)

    # Collate validate starting points for each block
    starts = { k:[] for k in range(0,len(counts)) }
    for i in range(0, len(counts)):
        length = counts[i]
        # Mandatory blocks
        for k,v in mandatory.items():
            if v==length:
                starts[i].append(k)
        # Mixed blocks
        for k,v in mixed.items():
            if length in v:
                starts[i].append(k)
        # Optional blocks
        for k,v in optional.items():
            if length in v:
                starts[i].append(k)
        #print(f"starts[ {i} ] =",starts[i])
    
    # Place the blocks
    placements = get_placements(starts, counts, 0)
    #print(placements)
    #print(json.dumps(placements,indent=3))
    
    # Check that all mandatory blocks have been used
    # TO-DO

    perms = count_permutations(placements)
    #print(json.dumps(perms,indent=3))

    return perms

def pattern_counts_7(pattern, counts):
    if pattern+" "+(",".join([str(n) for n in counts])) in CACHE.keys():
        return CACHE[pattern+" "+(",".join([str(n) for n in counts]))]
    #print("pattern_counts_7",pattern,counts)
    if len(counts) == 0:
        if pattern.count("#") == 0:
            return 1 # No remaining mandatory blocks, all requirements met, valid scenario
        else:
            return 0 # Mandatory blocks not used
    length = counts[0]
    total = 0
    for i in range(0, len(pattern)-sum(counts)-len(counts)+2):
        partial = pattern[i:i+length]
        #print(f"  starting from {i}, needing length {length}, found partial",partial)
        if partial.count(".") == 0 and pattern[:i].count("#") == 0:
            # The sub-string fits the first pattern!
            # If it isn't followed by a '#', keep going
            if i+length == len(pattern) or pattern[i+length] != "#":
                new_counts = counts[1:]
                x = pattern_counts_7(pattern[i+length+1:], new_counts)
                CACHE[ pattern[i+length+1:]+" "+(",".join([str(n) for n in new_counts])) ] = x
                total += x
    return total

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    #        0123456789-123456
    #data = ["?#???.#??#?????.? 3,1,3,1,1"]
    size=5
    total = 0

    if size==1:
        for r in range(0, len(data)):
        #for r in range(1,2):
            pattern, counts = data[r].split(" ")

            # Solve pattern 1
            counts = [int(n) for n in counts.split(",")]
            print(f"Pattern {r}: {pattern} counts {counts}")
            res = pattern_counts_7(pattern, counts)
            CACHE.clear()

            print(f"  ->",res, "total time so far:",int(time.time()-T))
            total += res
        print(total)
    if size==2:
        for r in range(0, len(data)):
            pattern, counts = data[r].split(" ")
            counts2 = counts+","+counts
            pattern2 = pattern+"?"+pattern

            # Solve pattern 2
            counts2 = [int(n) for n in counts2.split(",")]
            print(f"Pattern {r}: {pattern2} counts {counts2}")
            res = pattern_counts_7(pattern2, counts2)
            CACHE.clear()
            other = 0 #pattern_counts(pattern2, counts_to_goal(counts2))

            print(f"  ->",res, other, "total time so far:",int(time.time()-T))
            total += res
        print(total)
    if size==5:
        for r in range(0, len(data)):
            pattern, counts = data[r].split(" ")
            counts5 = counts+","+counts+","+counts+","+counts+","+counts
            pattern5 = pattern+"?"+pattern+"?"+pattern+"?"+pattern+"?"+pattern

            # Solve pattern 2
            counts5 = [int(n) for n in counts5.split(",")]
            print(f"Pattern {r}: {pattern5} counts {counts5}")
            res = pattern_counts_7(pattern5, counts5)
            CACHE.clear()

            print(f"  ->",res, "total time so far:",int(time.time()-T))
            total += res
        print(total)

#part1()
part2()
# For test data, 525152
# 316055368812 is too low
# 1220017367787 is too low
print((time.time()-T),"seconds")

"""
c = "?###????????"
c = "????.######..#####."
c = ".??.?#??##???."
a,b = pattern_counts(c, [1,6])
print("a",a)
d = c+"?"+c
e,f = pattern_counts(d, [1,6,1,6])
print("e",e)
g = c+"?"+c+"?"+c
h,i = pattern_counts(g, [1,6,1,6,1,6])
print("h",h)
j = c+"?"+c+"?"+c+"?"+c
k,l = pattern_counts(j, [1,6,1,6,1,6,1,6])
print("k",k)
m = c+"?"+c+"?"+c+"?"+c+"?"+c
n,o = pattern_counts(m, [1,6,1,6,1,6,1,6,1,6])
print("n",n)

a 5
e 47
h 455
k 4409
n 42725

42725/5**2 => 1709
47**2 => 2209
5**2 = 25
5**3 = 125
5**4 = 625
5**5 = 3125
# (47**2-5**4+5**3)*(5**2)

# 47*42*5*5-42*42*5+42*5*5*2+5**3-5**2-5
# b*b*a*a-(b-a)*(b-a)*a+(b-a)*a*a*2+a**3-a**2-a

39037.448


# 506250/150 = 3375

#150 150 10
#10 150 150
#150 10 150
# 150*150*1.5*15
# 150*150*(150/10)*(150/(10**2))

#res2**4 / res1**3

print(e**4 / a**3)

print(a * e**2)

# 2.25*10*(150**2)

# 4*(20/4)**4


Pattern 0: .??.?#??##???.?.??.?#??##???.?.??.?#??##???.?.??.?#??##???.?.??.?#??##???. counts [1, 6, 1, 6, 1, 6, 1, 6, 1, 6]
  -> 42725 total time so far: 3
Pattern 1: ?#???.#??#?????.???#???.#??#?????.???#???.#??#?????.???#???.#??#?????.???#???.#??#?????.? counts [3, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 3, 1, 1]
  -> 1259712 total time so far: 103
Pattern 2: ??#????#??#???.?????#????#??#???.?????#????#??#???.?????#????#??#???.?????#????#??#???.?? counts [4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1]
  -> 3498125 total time so far: 291
Pattern 3: ??#?.?#?#???#?#?????#?.?#?#???#?#?????#?.?#?#???#?#?????#?.?#?#???#?#?????#?.?#?#???#?#?? counts [1, 11, 1, 11, 1, 11, 1, 11, 1, 11]
  -> 32 total time so far: 291
Pattern 4: ?????????????????????????????????????????????????????? counts [1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1]
  -> 3268760 total time so far: 18488
Pattern 5: ?#?#????..????????#?#????..????????#?#????..????????#?#????..????????#?#????..?????? counts [6, 4, 6, 4, 6, 4, 6, 4, 6, 4]
  -> 60000 total time so far: 18502
Pattern 6: ?#?#?.#?#???????..???#?#?.#?#???????..???#?#?.#?#???????..???#?#?.#?#???????..???#?#?.#?#???????..? counts [5, 1, 1, 3, 2, 1, 5, 1, 1, 3, 2, 1, 5, 1, 1, 3, 2, 1, 5, 1, 1, 3, 2, 1, 5, 1, 1, 3, 2, 1]
  -> 1 total time so far: 18503
Pattern 7: ?.#??#??.??????.???.#??#??.??????.???.#??#??.??????.???.#??#??.??????.???.#??#??.??????.? counts [6, 1, 1, 1, 6, 1, 1, 1, 6, 1, 1, 1, 6, 1, 1, 1, 6, 1, 1, 1]
  -> 35840000 total time so far: 20446
Pattern 8: ##???###?.##???##???###?.##???##???###?.##???##???###?.##???##???###?.##?? counts [2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2]
  -> 32 total time so far: 20446
Pattern 9: ???.#??#????.???????.#??#????.???????.#??#????.???????.#??#????.???????.#??#????.??? counts [3, 7, 2, 3, 7, 2, 3, 7, 2, 3, 7, 2, 3, 7, 2]
  -> 162 total time so far: 20446
Pattern 10: ????#??..?#?????#??..?#?????#??..?#?????#??..?#?????#??..?# counts [1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1]
  -> 11508 total time so far: 20447
Pattern 11: .?..#????????#??????.?..#????????#??????.?..#????????#??????.?..#????????#??????.?..#????????#????? counts [1, 5, 6, 1, 5, 6, 1, 5, 6, 1, 5, 6, 1, 5, 6]
  -> 125951 total time so far: 20473
Pattern 12: ?#..??##??.?????#..??##??.?????#..??##??.?????#..??##??.?????#..??##??.??? counts [1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2]
  -> 5184 total time so far: 20473
Pattern 13: ?#???#???#??#???#???#??#???#???#??#???#???#??#???#???# counts [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]
  -> 16 total time so far: 20473
Pattern 14: #???#??..?????.??.?.?#???#??..?????.??.?.?#???#??..?????.??.?.?#???#??..?????.??.?.?#???#??..?????.??.?. counts [5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1]
  -> 28672 total time so far: 34059
Pattern 15: ??#??.?#??????.???#??.?#??????.???#??.?#??????.???#??.?#??????.???#??.?#??????. counts [2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1]
  -> 1964018 total time so far: 41022

  
Pattern 0: .??.?#??##???.?.??.?#??##???.?.??.?#??##???.?.??.?#??##???.?.??.?#??##???. counts [1, 6, 1, 6, 1, 6, 1, 6, 1, 6]
  -> 42725 total time so far: 0
Pattern 1: ?#???.#??#?????.???#???.#??#?????.???#???.#??#?????.???#???.#??#?????.???#???.#??#?????.? counts [3, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 3, 1, 1, 3, 1, 3, 1, 1]
  -> 1259712 total time so far: 3
Pattern 2: ??#????#??#???.?????#????#??#???.?????#????#??#???.?????#????#??#???.?????#????#??#???.?? counts [4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1]
  -> 3498125 total time so far: 7
Pattern 3: ??#?.?#?#???#?#?????#?.?#?#???#?#?????#?.?#?#???#?#?????#?.?#?#???#?#?????#?.?#?#???#?#?? counts [1, 11, 1, 11, 1, 11, 1, 11, 1, 11]
  -> 32 total time so far: 7
Pattern 4: ?????????????????????????????????????????????????????? counts [1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1, 1, 4, 1]
  -> 3268760 total time so far: 12
Pattern 5: ?#?#????..????????#?#????..????????#?#????..????????#?#????..????????#?#????..?????? counts [6, 4, 6, 4, 6, 4, 6, 4, 6, 4]
  -> 60000 total time so far: 12
Pattern 6: ?#?#?.#?#???????..???#?#?.#?#???????..???#?#?.#?#???????..???#?#?.#?#???????..???#?#?.#?#???????..? counts [5, 1, 1, 3, 2, 1, 5, 1, 1, 3, 2, 1, 5, 1, 1, 3, 2, 1, 5, 1, 1, 3, 2, 1, 5, 1, 1, 3, 2, 1]
  -> 1 total time so far: 12
Pattern 7: ?.#??#??.??????.???.#??#??.??????.???.#??#??.??????.???.#??#??.??????.???.#??#??.??????.? counts [6, 1, 1, 1, 6, 1, 1, 1, 6, 1, 1, 1, 6, 1, 1, 1, 6, 1, 1, 1]
  -> 35840000 total time so far: 71
Pattern 8: ##???###?.##???##???###?.##???##???###?.##???##???###?.##???##???###?.##?? counts [2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2, 2, 4, 2]
  -> 32 total time so far: 71
Pattern 9: ???.#??#????.???????.#??#????.???????.#??#????.???????.#??#????.???????.#??#????.??? counts [3, 7, 2, 3, 7, 2, 3, 7, 2, 3, 7, 2, 3, 7, 2]
  -> 162 total time so far: 71
Pattern 10: ????#??..?#?????#??..?#?????#??..?#?????#??..?#?????#??..?# counts [1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1]
  -> 11508 total time so far: 72
Pattern 11: .?..#????????#??????.?..#????????#??????.?..#????????#??????.?..#????????#??????.?..#????????#????? counts [1, 5, 6, 1, 5, 6, 1, 5, 6, 1, 5, 6, 1, 5, 6]
  -> 125951 total time so far: 72
Pattern 12: ?#..??##??.?????#..??##??.?????#..??##??.?????#..??##??.?????#..??##??.??? counts [1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2, 1, 5, 2]
  -> 5184 total time so far: 72
Pattern 13: ?#???#???#??#???#???#??#???#???#??#???#???#??#???#???# counts [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2]
  -> 16 total time so far: 72
Pattern 14: #???#??..?????.??.?.?#???#??..?????.??.?.?#???#??..?????.??.?.?#???#??..?????.??.?.?#???#??..?????.??.?. counts [5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1, 5, 1, 1, 1, 2, 1]
  -> 28672 total time so far: 72
Pattern 15: ??#??.?#??????.???#??.?#??????.???#??.?#??????.???#??.?#??????.???#??.?#??????. counts [2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 1, 1, 1]
  -> 1964018 total time so far: 98
"""
