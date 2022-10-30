import time
# Test data
# First to last 0,3,6,0,3,3,1,0,4,0
# Last to first 0,4,0,1,3,3,0,3,6,0

""" Part 2:
A stack of 30000000 items was going to be too slow to process.
Much quicker to have a hash table of the different values and the last time they were used, as that is all that is actually needed. A much smaller dataset I expect.
"""
def part2(puzzle, stop_point):
    turn = 0
    seen = {}
    for i in range(len(puzzle)):
        turn += 1
        last = puzzle[i]
        seen[last] = turn
    next = 0
    while turn < stop_point-1:
        turn += 1 
        if not next in seen.keys():
            #print(f"Setting seen[{next}] to {turn}. Next number is 0")
            seen[next] = turn
            next = 0
        else:
            #print(f"Turn {turn}, next {next}, seen[{next}] {seen[next]}")
            diff = turn - seen[next]
            #print(f"Setting seen[{next}] to {turn}. Next number is {diff}")
            seen[next] = turn
            next = diff
        #print(seen)
        if turn % 1000000 == 0:
            print("Turn",turn)
    # print(stack)
    print(f"Turn {turn+1} is {next}")
    print(f"Final dataset had {len(seen)} items.")

def part1(puzzle, stop_point):
    turn = 0
    stack = []
    for i in range(len(puzzle)):
        stack.insert(0, puzzle[i])
        turn += 1
    while turn < stop_point:
        last_number = stack[0]
        # print("turn ",turn," last ",last_number," stack ",stack[1:])
        if not last_number in stack[1:]:
            stack.insert(0,0)
        else:
            most_recent = stack[1:].index(last_number) +1
            diff = most_recent
            stack.insert(0, diff)
        if turn % 1000000 == 0:
            print("Turn",turn)
        turn += 1 
    if len(stack) < 2500:
        print(stack)
    print(f"Turn {turn} is {stack[0]}")

puzzle = [0,3,6] # Turn 10 is 0
puzzle = [1,3,2] # Turn 2020 is 1
puzzle = [2,3,1] # Turn 2020 is 78
puzzle = [3,1,2] # Turn 2020 is 1836
puzzle = [1,17,0,10,18,11,6] # Turn 2020 is 595, turn 30000000 is 1708310
part1(puzzle, 2020)
t1 = time.time()
part2(puzzle, 30000000)
t2 = time.time()
print(f"Part 2: Time taken {t2-t1} seconds")
