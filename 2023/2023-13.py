
FILE = "./2023/2023-13.txt"

TEST = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".splitlines()

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    # Split data into individual tests
    tests = [[]]
    test_idx = 0
    for i in range(0, len(data)):
        if data[i] == "":
            test_idx += 1
            tests.append([])
        else:
            tests[test_idx].append(data[i])
    #print(tests)
    total = 0
    for t in range(0, len(tests)):
        # Test for vertical
        for r in range(0, len(tests[t])-1):
            if tests[t][r] == tests[t][r+1]: # Possible candidate for reflective point
                offset = 0
                reflection = True
                while r-offset >= 0 and r+1+offset < len(tests[t]):
                    if tests[t][r-offset] != tests[t][r+1+offset]:
                        reflection = False
                        break
                    offset += 1
                if reflection:
                    print(f"Test {t}: Found reflection at row {r+1}")
                    total += 100*(r+1)
        # Test for horizontal
        for c in range(0, len(tests[t][0])-1):
            col1 = ""
            col2 = ""
            for r in range(0, len(tests[t])):
                col1 += tests[t][r][c]
                col2 += tests[t][r][c+1]
            if col1 == col2: # Possible candidate for reflective point
                offset = 0
                reflection = True
                while c-offset >= 0 and c+1+offset < len(tests[t][0]):
                    col1 = ""
                    col2 = ""
                    for r in range(0, len(tests[t])):
                        col1 += tests[t][r][c-offset]
                        col2 += tests[t][r][c+1+offset]
                    if col1 != col2:
                        reflection = False
                        break
                    offset += 1
                if reflection:
                    print(f"Test {t}: Found reflection at column {c+1}")
                    total += (c+1)
    print(total)

def create_reflection_x(data, x):
    out1 = "" 
    out2 = ""
    for r in range(0, len(data)):
        out1 += data[r][x]
        out2 += data[r][x+1]
    offset = 1
    while x-offset >= 0 and x+1+offset < len(data[r]):
        for r in range(0, len(data)):
            out1 += data[r][x-offset]
            out2 += data[r][x+1+offset]
        offset += 1
    return out1, out2

def create_reflection_y(data, y):
    out1 = data[y] 
    out2 = data[y+1]
    offset = 1
    while y-offset >= 0 and y+1+offset < len(data):
        out1 += data[y-offset] 
        out2 += data[y+1+offset]
        offset += 1
    return out1, out2

def str_match(s1, s2):
    stop = min(len(s1),len(s2))
    no_match = 0
    for i in range(0, stop):
        if s1[i] != s2[i]: no_match+=1
    return True if no_match ==1 else False

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    # Split data into individual tests
    tests = [[]]
    test_idx = 0
    for i in range(0, len(data)):
        if data[i] == "":
            test_idx += 1
            tests.append([])
        else:
            tests[test_idx].append(data[i])
    #print(tests)
    total = 0
    for t in range(0, len(tests)):
    #for t in range(0, 10):
        found = False
        for y in range(0, len(tests[t])-1):
            r1,r2 = create_reflection_y(tests[t], y)
            print(t,y,r1,"\n   ",r2)
            if str_match(r1,r2) and not found:
                print(f"Test {t}: Found reflection at row {y+1}")
                total += 100*(y+1)
                found = True
        for x in range(0, len(tests[t][0])-1):
            c1,c2 = create_reflection_x(tests[t], x)
            if str_match(c1,c2) and not found:
                print(f"Test {t}: Found reflection at col {x+1}")
                total += x+1
                found = True
    print(total)
    
#part1()
# 37718

part2()
# 64056 too high
# 41597 too high
# 40995
