import time, math
from pprint import pprint

start = time.time()
with open("./2022/day5.txt", "r") as f:
    data = f.read().splitlines()

demo="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()

stacks = {}

def part1(data, line_for_bottom_of_stacks, number_of_stacks):
    stack_ids = data[line_for_bottom_of_stacks]
    # Create stacks
    for column in range(1, number_of_stacks+1):
        stacks[column] = []
    # Populate stacks
    for row in range(line_for_bottom_of_stacks,-1,-1):
        for column in range(1, number_of_stacks+1):
            # 1, 5, 
            char = 4*(column-1)+1
            if data[row][char].isalpha():
                stacks[column].append(data[row][char])
    pprint(stacks)
    # Process moves
    for row in range(line_for_bottom_of_stacks+3, len(data)):
        parts = data[row].split(" ") # "qty" is pos 1; "from" is pos 3; "to" is pos 5
        print(parts)
        qty = int(parts[1])
        src = int(parts[3])
        dest = int(parts[5])
        for q in range(0, qty):
            val = stacks[src].pop()
            stacks[dest].append(val)
    pprint(stacks)
    return True

def part2(data, line_for_bottom_of_stacks, number_of_stacks):
    stack_ids = data[line_for_bottom_of_stacks]
    # Create stacks
    for column in range(1, number_of_stacks+1):
        stacks[column] = []
    # Populate stacks
    for row in range(line_for_bottom_of_stacks,-1,-1):
        for column in range(1, number_of_stacks+1):
            char = 4*(column-1)+1
            if data[row][char].isalpha():
                stacks[column].append(data[row][char])
    pprint(stacks)
    # Process moves
    for row in range(line_for_bottom_of_stacks+3, len(data)):
        parts = data[row].split(" ") # qty 1, from 3 and to 5
        print(parts)
        qty = int(parts[1])
        src = int(parts[3])
        dest = int(parts[5])
        # Pick up
        tmp = []
        for q in range(0, qty):
            val = stacks[src].pop()
            tmp.append(val)
        # Put down
        for q in range(0, qty):
            val = tmp.pop()
            stacks[dest].append(val)
    pprint(stacks)
    return True

# part1(demo,2,3)
# part1(data,7,9)
# part2(demo,2,3)
part2(data,7,9)
print("Execution time:",time.time()-start)
