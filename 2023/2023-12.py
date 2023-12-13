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

def pattern_counts(pattern, counts):
    # Convert a counts 1,1,3 into a target string of #.#.###
    goal = ""
    for i in range(0, len(counts)):
        goal += "#"*counts[i]+"."
    goal = goal[:-1]
    # List of partial matches found so far
    matching = [""]
    cache = []
    full_matches = 0
    while len(matching) > 0:
        match = matching.pop()
        if len(match) == len(pattern):
            if is_pattern_full_match(match, goal):
                #print("          ",match,goal)
                full_matches += 1
                cache.append(match)
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
    return full_matches, cache

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    data = TEST
    total = 0
    # Round 1 - The small sized data
    #for r in range(0, len(data)):
    for r in range(0, len(data)):
        pattern, counts = data[r].split(" ")
        counts2 = counts+","+counts
        pattern2 = pattern+"?"+pattern

        # Solve pattern 1
        counts = [int(n) for n in counts.split(",")]
        print(f"Pattern {r}: {pattern} counts {counts}")
        a, _ = pattern_counts(pattern, counts)

        # Solve pattern 2
        counts2 = [int(n) for n in counts2.split(",")]
        print(f"Pattern {r}: {pattern2} counts {counts2}")
        b, _ = pattern_counts(pattern2, counts2)

        # Math it!
        print("a,b",a,b)
        #result = res2**4 / res1**3
        #result = a * (b/a) * (b/a) * (b/a) * (b/a)
        #result = (b**2 - a**4 + a**3) * (a**2)
        result = b*b*a*a-(b-a)*(b-a)*a+(b-a)*a*a*2+a**3-a**2-a

        print(f"  ->",result, "total time so far:",int(time.time()-T))
        if float(result) // 1.0 != float(result):
            print("Non integer result")
            exit()
        total += int(result)
    print(total)

#part1()
part2()
# For test data, 525152
# 316055368812 is too low
# 1220017367787 is too low
print(int(time.time()-T),"seconds")

#"""
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

"""
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
"""

# 506250/150 = 3375

#150 150 10
#10 150 150
#150 10 150
# 150*150*1.5*15
# 150*150*(150/10)*(150/(10**2))

#res2**4 / res1**3

print(e**4 / a**3)

print(a * e**2)

#"""
# 2.25*10*(150**2)

# 4*(20/4)**4
