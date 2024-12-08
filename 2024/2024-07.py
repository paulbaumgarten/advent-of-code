import math, random, numpy, os, re, copy, time

DEMO = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

def calc(expression):
    tokens = re.split(r'([+*])', expression)
    value = int(tokens[0])
    next_op = tokens[1]
    for i in range(2, len(tokens)):
        if tokens[i] == "+":
            next_op = "+"
        elif tokens[i] == "*":
            next_op = "*"
        else: # number
            if next_op == "+":
                value = value + int(tokens[i])
            else:
                value = value * int(tokens[i])
    return value

def part1(raw):
    data = DEMO[:]
    data = raw[:]
    total = 0
    for i in range(0, len(data)):
        # For this problem...
        # Build the permutations
        answer,problem = data[i].split(": ")
        answer = int(answer)
        attempts = []
        final_attempts = []
        attempts.append(problem)
        working = True
        while working:
            working = False
            new_attempts = []
            for j in range(0, len(attempts)):
                space = attempts[j].find(" ")
                if space < 0:
                    final_attempts.append(attempts[j])
                else:
                    new_attempts.append( attempts[j][:space]+"+"+attempts[j][space+1:] )
                    new_attempts.append( attempts[j][:space]+"*"+attempts[j][space+1:] )
                    working = True
            attempts = new_attempts[:]
        print(answer," = ",final_attempts)
        # Attempt each permutation
        for j in range(0, len(final_attempts)):
            if answer == calc(final_attempts[j]):
                print("Found match for ",answer," and ",final_attempts[j])
                total += answer
                break
    return total

def calc2(expression):
    tokens = re.split(r'([amj])', expression)
    value = int(tokens[0])
    next_op = tokens[1]
    for i in range(2, len(tokens)):
        if tokens[i] == "a":
            next_op = "a"
        elif tokens[i] == "m":
            next_op = "m"
        elif tokens[i] == "j":
            next_op = "j"
        else: # number
            if next_op == "a":
                value = value + int(tokens[i])
            elif next_op == "m":
                value = value * int(tokens[i])
            else: # join
                value = int(str(value) + tokens[i])
    return value

def part2(raw):
    data = DEMO[:]
    data = raw[:]
    total = 0
    for i in range(0, len(data)):
        # For this problem...
        # Build the permutations
        answer,problem = data[i].split(": ")
        answer = int(answer)
        attempts = []
        final_attempts = []
        attempts.append(problem)
        working = True
        while working:
            working = False
            new_attempts = []
            for j in range(0, len(attempts)):
                space = attempts[j].find(" ")
                if space < 0:
                    final_attempts.append(attempts[j])
                else:
                    new_attempts.append( attempts[j][:space]+"a"+attempts[j][space+1:] )
                    new_attempts.append( attempts[j][:space]+"m"+attempts[j][space+1:] )
                    new_attempts.append( attempts[j][:space]+"j"+attempts[j][space+1:] )
                    working = True
            attempts = new_attempts[:]
        #print(answer," = ",final_attempts)
        # Attempt each permutation
        for j in range(0, len(final_attempts)):
            if answer == calc2(final_attempts[j]):
                print("Found match for ",answer," and ",final_attempts[j])
                total += answer
                break
    return total

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


