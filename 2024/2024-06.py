import math, random, numpy, os, re, copy, time

DEMO = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

def part1(raw):
    #data = DEMO[:]
    data = raw[:]
    data = [list(x) for x in data]
    # Get start location
    loc = [0,0]
    dir = "up"
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == "^":
                loc = [y,x]
                break
    # Traverse
    inbounds = True
    unique = 0
    while inbounds:
        peak = loc[:]
        match dir:
            case "up": peak = [peak[0]-1, peak[1]]
            case "down": peak = [peak[0]+1, loc[1]]
            case "left": peak = [peak[0], peak[1]-1]
            case "right": peak = [peak[0], peak[1]+1]
        if peak[0] < 0 or peak[0] >= len(data) or peak[1] < 0 or peak[1] >= len(data[0]):
            inbounds = False
            break
        # If an obstacle, turn first
        if data[peak[0]][peak[1]] == "#":
            match dir:
                case "up": dir = "right"
                case "down": dir = "left"
                case "left": dir = "up"
                case "right": dir = "down"
            continue # Try again with the new direction
        # Move forward
        if data[loc[0]][loc[1]] == "." or data[loc[0]][loc[1]] == "^":
            unique += 1
            data[loc[0]][loc[1]] = "x"
        loc = peak[:]
        if data[loc[0]][loc[1]] == ".":
            unique += 1
            data[loc[0]][loc[1]] = "x"
    return unique

def add_direction_to_value(val, dir):
    if val == ".": val = "0"
    val = int(val,16)
    match dir:
        case "up": val += 1
        case "down": val += 2
        case "left": val += 8
        case "right": val += 4
    val = hex(val)[2:]
    return val

def get_directions_visited(val):
    try:
        val = int(val, 16)
        up = val & 1
        down = val & 2
        left = val & 8
        right = val & 4
        return (left,right,down,up)
    except:
        return (0,0,0,0)

def traverse_until_loop_or_exit(raw, obstacle):
    # Traversal values
    # bits    4-3-2-1
    # meaning L-R-D-U
    # Get start location
    data = copy.deepcopy(raw)
    loc = [0,0]
    dir = "up"
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == "^":
                loc = [y,x]
                break
    data[loc[0]][loc[1]] = "1"

    # Add the obstacle
    if obstacle == loc:
        return False
    data[obstacle[0]][obstacle[1]] = "#"

    # Traverse
    inbounds = True
    loop = False
    unique = 0
    move = 0
    while inbounds and (not loop):
        # Progress indicator to troubleshoot
        move += 1
        if move % 1000000 == 0: print("For obstacle",obstacle," processing move #",move)
        # Let's go!
        peak = loc[:]
        match dir:
            case "up": peak = [peak[0]-1, peak[1]]
            case "down": peak = [peak[0]+1, loc[1]]
            case "left": peak = [peak[0], peak[1]-1]
            case "right": peak = [peak[0], peak[1]+1]
        if peak[0] < 0 or peak[0] >= len(data) or peak[1] < 0 or peak[1] >= len(data[0]):
            inbounds = False
            break
        # If an obstacle, turn first
        peak_value = data[peak[0]][peak[1]]
        if peak_value == "#":
            match dir:
                case "up": dir = "right"
                case "down": dir = "left"
                case "left": dir = "up"
                case "right": dir = "down"
            continue # Try again with the new direction
        # Prior to moving forward, have we already moved in that direction for that location (indicating the start of a loop)?
        previous_movement = get_directions_visited(peak_value)
        if (dir=="up" and previous_movement[3]) or \
            (dir=="down" and previous_movement[2]) or \
            (dir=="left" and previous_movement[0]) or \
            (dir=="right" and previous_movement[1]):
            print("Loop detected at location ",peak)
            loop = True
            break
        # Move forward
        loc = peak[:]
        if data[loc[0]][loc[1]] == ".":
            unique += 1
            data[loc[0]][loc[1]] = add_direction_to_value(data[loc[0]][loc[1]], dir)
    return loop

def part2(raw):
    data = raw[:]
    #data = DEMO[:]
    data = [list(x) for x in data]
    loops = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            #print("y",y,"x",x,end=" ")
            loop = traverse_until_loop_or_exit(data, (y,x))
            #print(loop)
            if loop:
                loops += 1
    return loops

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")

