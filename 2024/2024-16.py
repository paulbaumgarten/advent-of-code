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

def show_grid2(grid):
    print("   ",end="")
    for x in range(0, len(grid[0])):
        print(f"{(x % 10)}", end=" ")
    print()
    for y in range(len(grid)):
        print(f"{y:2} ",end="")
        for x in range(0, len(grid[y])):
            val = str(grid[y][x])
            print(f"{ val.ljust(2," ") }",end="")
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

def find_blocks_on_optimal(grid, start, finish):
    timer = time.time()
    y,x = start
    grid[finish[0]][finish[1]] = "."
    costs = [[ math.inf for x in range(len(grid[0]))] for y in range(len(grid))]
    dir = [[ "x" for x in range(len(grid[0]))] for y in range(len(grid))]
    costs2 = [[ {"v":math.inf, "<":math.inf, ">":math.inf, "^":math.inf} for x in range(len(grid[0]))] for y in range(len(grid))]
    costs[y][x] = 0
    costs2[y][x][">"] = 0
    dir[y][x] = ">"
    q = []
    q.append( [y,x] )
    routes = []
    current_dir = ">"
    current_cost = 0
    while len(q) > 0:
        y,x = q.pop(0)
        #print(y,x,len(q))
        for current_dir in ["^",">","<","v"]:
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
                    if costs2[y2][x2][k] > (costs2[y][x][current_dir] + this_cost):
                        costs2[y2][x2][k] = costs2[y][x][current_dir] + this_cost
                        q.append([y2,x2])
    final_cost = min(costs2[finish[0]][finish[1]]["v"],costs2[finish[0]][finish[1]]["<"],costs2[finish[0]][finish[1]][">"],costs2[finish[0]][finish[1]]["^"])

    print(f"Finding blocks on paths that cost {final_cost}")
    block_count = 0
    unique_blocks_optimal_path = set()
    # Traverse all the path options, and if it is an optimal path, add those blocks to the set.
    y,x = start[:]
    q = [[y,x,0,">",f"({y},{x}) "]]
    paths = [[ "" for x in range(len(grid[0]))] for y in range(len(grid))]
    paths_to_finish = []
    while len(q) > 0:
        y,x,cost,current_dir,path = q.pop(0)
        #print("len(q)=",len(q),"y,x=",y,x,"path=",path)
        #current_dir = dir[y][x]
        if time.time()-timer > 10:
            print("len(q)=",len(q),"y,x=",y,x)
            timer = time.time()
        if [y,x] == finish:
            pairs = path.split(" ")
            paths_to_finish.append(path)
            print("adding path to finish line #",len(paths_to_finish))
            for pair in pairs:
                if pair != "":
                    unique_blocks_optimal_path.add(pair)
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
                if ((cost + this_cost) <= final_cost) and (cost+this_cost<=costs2[y2][x2][k]):
                    this_loc = f"({y2},{x2}) "
                    if this_loc not in path:
                        tmp = path + this_loc
                        q.append([y2,x2,cost+this_cost,k,tmp])
    #print(f"Unique blocks {len(unique_blocks_optimal_path)}, listing...\n",unique_blocks_optimal_path)
    #print(f"paths to finish {len(paths_to_finish)}:...\n","\n\n".join(paths_to_finish))
    return len(unique_blocks_optimal_path)
    # 45, 64, 149, 85396

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
    data = EX2[:]
    data = raw[:]
    grid = [list(line) for line in data]
    start = locate_char(grid, "S")
    finish = locate_char(grid, "E")
    print(f"Searching for cheapest path from {start} to {finish}")
    blocks = find_blocks_on_optimal(grid, start, finish)
    return blocks

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


