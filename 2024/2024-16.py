import math, random, numpy, os, re, copy, time

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

EX1 = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".splitlines()
# 7036, 45

EX2 = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################""".splitlines()
# 11048, 64

EX3 = """###########################
#######################..E#
######################..#.#
#####################..##.#
####################..###.#
###################..##...#
##################..###.###
#################..####...#
################..#######.#
###############..##.......#
##############..###.#######
#############..####.......#
############..###########.#
###########..##...........#
##########..###.###########
#########..####...........#
########..###############.#
#######..##...............#
######..###.###############
#####..####...............#
####..###################.#
###..##...................#
##..###.###################
#..####...................#
#.#######################.#
#S........................#
###########################""".splitlines()
# 21148, 149

### Today's problem

def locate_char(grid, target):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == target:
                return [y,x]

def show_grid(grid):
    print("   ",end="")
    for x in range(0, len(grid[0])):
        print(f"{(x % 10)}:4", end="")
    print()
    for y in range(len(grid)):
        print(f"{y:02} ",end="")
        for x in range(0, len(grid[y])):
            val = str(grid[y][x] // 1000)
            print(f"{ val.ljust(3," ") }",end=" ")
        print()
    print()

def find_cheapest(grid, start, finish):
    y,x = start
    grid[finish[0]][finish[1]] = "."
    costs = [[ math.inf for x in range(len(grid[0]))] for y in range(len(grid))]
    dir = [[ "x" for x in range(len(grid[0]))] for y in range(len(grid))]
    costs[y][x] = 0
    dir[y][x] = ">"
    q = []
    q.append( [y,x] )
    routes = []
    current_dir = ">"
    current_cost = 0
    while len(q) > 0:
        y,x = q.pop(0)
        #print(y,x,len(q))
        current_dir = dir[y][x]
        if current_dir == "<":
            options = {"<": [y, x-1, 1], "^": [y-1, x, 1001], "v": [y+1, x, 1001]}
        elif current_dir == "^":
            options = {"^": [y-1, x, 1], "<": [y, x-1, 1001], ">": [y, x+1, 1001]}
        elif current_dir == ">":
            options = {">": [y, x+1, 1], "^": [y-1, x, 1001], "v": [y+1, x, 1001]}
        else:
            options = {"v": [y+1, x, 1], "<": [y, x-1, 1001], ">": [y, x+1, 1001]}
        for k, v in options.items():
            y2, x2, this_cost = v
            if grid[y2][x2] != "#":
                if costs[y2][x2] > (costs[y][x] + this_cost):
                    costs[y2][x2] = costs[y][x] + this_cost
                    dir[y2][x2] = k
                    q.append([y2,x2])
    show_grid(costs)
    return costs[finish[0]][finish[1]]
    return None

def part1(raw):
    data = EX3[:]
    data = raw[:]
    grid = [list(line) for line in data]
    start = locate_char(grid, "S")
    finish = locate_char(grid, "E")
    print(f"Searching for cheapest path from {start} to {finish}")
    cost = find_cheapest(grid, start, finish)
    return cost
    # 89400 is too high

def part2(raw):
    pass

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


