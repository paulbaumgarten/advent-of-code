# 18.py
import re

def solve(problem):
    #print("Solving: ",problem)
    while "(" in problem:
        # We might have several sets of nested parenthesis...
        closing = problem.index(")") # Find the first closing parenthesis
        opening = problem[:closing].rindex("(") # Find the first opening before the closing one
        tmp = solve(problem[opening+1:closing])
        problem = problem[:opening] + str(tmp) + problem[closing+1:]
        #print("Problem now ",problem)
    val = 0
    parts = problem.split(" ")
    val = int(parts[0])
    i = 1
    while i < len(parts)-1:
        if parts[i] == "+":
            val = val + int(parts[i+1])
        elif parts[i] == "*":
            val = val * int(parts[i+1])
        i+=2
    #print("Returning ",val)
    return val

def solve2(problem):
    #print("Solving: ",problem)
    while "(" in problem:
        # We might have several sets of nested parenthesis...
        closing = problem.index(")") # Find the first closing parenthesis
        opening = problem[:closing].rindex("(") # Find the first opening before the closing one
        tmp = solve2(problem[opening+1:closing])
        problem = problem[:opening] + str(tmp) + problem[closing+1:]
        #print("Problem now ",problem)
    val = 0
    parts = problem.split(" ")
    while "+" in parts:
        op_location = parts.index("+")
        val1 = parts[op_location-1]
        val2 = parts[op_location+1]
        new_val = int(val1) + int(val2)
        parts.pop(op_location-1)
        parts.pop(op_location-1)
        parts.pop(op_location-1)
        parts.insert(op_location-1, new_val)
    while "*" in parts:
        op_location = parts.index("*")
        val1 = parts[op_location-1]
        val2 = parts[op_location+1]
        new_val = int(val1) * int(val2)
        parts.pop(op_location-1)
        parts.pop(op_location-1)
        parts.pop(op_location-1)
        parts.insert(op_location-1, new_val)

    #print("Returning ",parts)
    return parts[0]

def part1(problems):
    r = 0
    for problem in problems:
        print(f"{problem}...",end="")
        a = solve(problem)
        r += a
        print(a)
    return r

def part2(problems):
    r = 0
    for problem in problems:
        print(f"{problem}...",end="")
        a = solve2(problem)
        r += a
        print(a)
    return r

with open("18.txt", "r") as f:
    content = f.read().splitlines()

r = part1(content)
print(f"Part 1 = {r}")
r = part2(content)
print(f"Part 2 = {r}")
