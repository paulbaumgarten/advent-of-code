import time, math
from pprint import pprint

def move_tail(head, tail):
    print(f"    move_tail: head: {head} tail: {tail}",end="")
    dy = abs(head[0]-tail[0])
    dx = abs(head[1]-tail[1])
    if (dx==0 and dy==2) or (dy==0 and dx==2) or (dx==2 and dy==2):
        y = (head[0]-tail[0]) // 2
        x = (head[1]-tail[1]) // 2
        tail = (tail[0]+y, tail[1]+x)
    elif (dy==1 and dx==2):
        if head[1]>tail[1]: # Go right and up/down
            tail = (head[0] , tail[1] + 1)
        else: # Go left and up/down
            tail = (head[0] , tail[1] - 1)
    elif (dx==1 and dy==2):
        if head[0]>tail[0]:
            tail = (tail[0] + 1, head[1])
        else:
            tail = (tail[0] - 1, head[1])
    elif (dx<=1 and dy<=1):
        pass
    else:
        print(f"\nNot sure what we are doing here. Help. head: {head} tail: {tail}")
        exit()
    print(f" now tail: {tail}")
    return tail

def part1(data):
    head = (0,0)
    tail = (0,0)
    history = {}
    snake = []
    for move in range(0, len(data)):
        op, steps = data[move].split(" ")
        steps = int(steps)
        print(f"Head is at {head}, tail is at {tail}, move {op} by {steps} steps.")
        for s in range(0, steps):
            if op=="U":
                head = (head[0]-1, head[1])
            if op=="D":
                head = (head[0]+1, head[1])
            if op=="L":
                head = (head[0], head[1]-1)
            if op=="R":
                head = (head[0], head[1]+1)
            #print(f"  step {s} Head now at {head}, tail is at {tail}.")
            tail = move_tail(head, tail)
            # Record location of tail
            if tail[0] not in history.keys():
                history[ tail[0] ] = {}
            history[ tail[0] ][ tail[1] ] = "#"
        # end for each step
    c = 0
    #pprint(history)
    for k,v in history.items():
        for k2,v2 in v.items():
            c += 1
    return c

def part2(data):
    history = {}
    snake = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    piece_to_record = len(snake)-1
    for move in range(0, len(data)):
        op, steps = data[move].split(" ")
        steps = int(steps)
        print(f"Head is at {snake[0]}, tail is at {snake[len(snake)-1]}, move {op} by {steps} steps. (#{move})")
        for s in range(0, steps):
            if op=="U":
                snake[0] = (snake[0][0]-1, snake[0][1])
            if op=="D":
                snake[0] = (snake[0][0]+1, snake[0][1])
            if op=="L":
                snake[0] = (snake[0][0], snake[0][1]-1)
            if op=="R":
                snake[0] = (snake[0][0], snake[0][1]+1)
            print(f"  step {s} - Head now at {snake[0]}, tail is at {snake[len(snake)-1]}.")
            for body_part in range(1,len(snake)):
                snake[body_part] = move_tail(snake[body_part-1], snake[body_part])
            print("    ",snake)
            # Record location of tail
            if snake[piece_to_record][0] not in history.keys():
                history[ snake[piece_to_record][0] ] = {}
            history[ snake[piece_to_record][0] ][ snake[piece_to_record][1] ] = "#"
        # end for each step
    c = 0
    # pprint(history)
    for k,v in history.items():
        for k2,v2 in v.items():
            c += 1
    return c

#####################################
start = time.time()
with open("./2022/day9b.txt", "r") as f:
    data = f.read().splitlines()
#print("part 1 = ",part1(data)) # 6745
print("*"*50)
print("part 2 = ",part2(data))
print("Execution time:",time.time()-start)
