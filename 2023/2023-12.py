
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

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    data = TEST2
    total = 0
    for r in range(0, len(data)):
    #for r in range(1, 2):
        pattern, counts = data[r].split(" ")
        # Unfold the data .... 5 copies! eek
        pre_pattern = "?"+pattern
        post_pattern = pattern+"?"
        orig_pattern = pattern
        #pattern = ((pattern + "?") * 5)[:-1]
        #simple_pattern = pattern + "."
        #while simple_pattern.count("..") > 0:
        #    simple_pattern = simple_pattern.replace("..",".")
        #counts = ((counts + ",") * 5)[:-1]
        # Now let's work        
        counts = [int(n) for n in counts.split(",")]
        # What is the target patten?
        target = ""
        for k in range(0, len(counts)):
            target += "#"*counts[k]
            if k < len(counts)-1:
                target += "."
        print(pattern, counts, target)
        #print(simple_pattern)
        #print(target)
        # Calculate the permuations
        matches_this_pattern = count_patterns_match_target(pattern, target)
        print(matches_this_pattern)
        matches_this_pattern_pre = count_patterns_match_target(pre_pattern, target)
        print(matches_this_pattern_pre)
        matches_this_pattern_post = count_patterns_match_target(post_pattern, target)
        print(matches_this_pattern_post)
        #if matches_this_pattern==matches_this_pattern_post or matches_this_pattern==matches_this_pattern_pre: # the additional '?' must be used as a '.'
        #    total += matches_this_pattern**5
        #else:
        total += max(matches_this_pattern_pre,matches_this_pattern_post)**4 * matches_this_pattern
    print(total)
    
#part1()
part2()
# 316055368812 is too low


