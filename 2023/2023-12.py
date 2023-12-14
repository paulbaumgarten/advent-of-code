import functools
import time

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

@functools.cache
def pattern_counts_r(pattern, goal):
    # List of partial matches found so far
    full_matches = 0

    match = ""
    if len(match) == len(pattern):
        if is_pattern_full_match(match, goal):
            return 1
        else:
            return 0
    else:
        next_char = pattern[len(match)]
        if next_char == "#":
            if is_pattern_partial_match(match+"#", goal):
                full_matches += pattern_counts_r(match+"#", goal)
        if next_char == ".":
            if is_pattern_partial_match(match+".", goal):
                full_matches += pattern_counts_r(match+".", goal)
        if next_char == "?":
            if is_pattern_partial_match(match+"#", goal):
                full_matches += pattern_counts_r(match+"#", goal)
            if is_pattern_partial_match(match+".", goal):
                full_matches += pattern_counts_r(match+".", goal)
    return full_matches

def counts_to_goal(counts):
    # Convert a counts 1,1,3 into a target string of #.#.###
    goal = ""
    for i in range(0, len(counts)):
        goal += "#"*counts[i]+"."
    goal = goal[:-1]
    return goal

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    total = 0
    # Round 1 - The small sized data
    #for r in range(0, len(data)):
    for r in range(0, len(data)):
        pattern, counts = data[r].split(" ")
        counts2 = counts+","+counts+","+counts+","+counts+","+counts
        pattern2 = pattern+"?"+pattern+"?"+pattern+"?"+pattern+"?"+pattern

        # Solve pattern 1
        #counts = [int(n) for n in counts.split(",")]
        #print(f"Pattern {r}: {pattern} counts {counts}")
        #a = pattern_counts(pattern, counts_to_goal(counts))

        # Solve pattern 2
        counts2 = [int(n) for n in counts2.split(",")]
        print(f"Pattern {r}: {pattern2} counts {counts2}")
        b = pattern_counts(pattern2, counts_to_goal(counts2))

        # Math it!
        #result = res2**4 / res1**3
        #result = a * (b/a) * (b/a) * (b/a) * (b/a)
        #result = (b**2 - a**4 + a**3) * (a**2)
        result = b

        print(f"  ->",result, "total time so far:",int(time.time()-T))
        total += int(result)
    print(total)

#part1()
part2()
# For test data, 525152
# 316055368812 is too low
# 1220017367787 is too low
print(int(time.time()-T),"seconds")

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
  
"""
