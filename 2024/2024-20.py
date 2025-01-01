import math, random, numpy, os, re, copy, time
from pprint import pprint

EX1 = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def find_char(grid, c):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == c:
                return [y,x]
    return None

def get_coords_of_manhattan_distance(orig, dist):
    y,x = orig
    res = []
    for offset in range(0, dist):
        res.append([y+offset,x+dist-offset])
        res.append([y-offset,x+dist-offset])
        res.append([y+dist-offset,x-offset])
        res.append([y+dist-offset,x+offset])
        res.append([y+offset,x-dist+offset])
        res.append([y-offset,x-dist+offset])
        res.append([y-dist+offset,x-offset])
        res.append([y-dist+offset,x+offset])
    res2 = []
    for r in res:
        if r not in res2:
            res2.append(r)
    return res2

def get_coords_upto_manhattan_distance(orig, max_dist):
    y,x = orig
    distances = []
    res = []
    for dist in range(1, max_dist+1):
        for offset in range(0, dist):
            res.append( [ y+offset, x+dist-offset, dist ] )
            res.append( [ y-offset, x+dist-offset, dist ] )
            res.append( [ y+dist-offset, x-offset, dist ] )
            res.append( [ y+dist-offset, x+offset, dist ] )
            res.append( [ y+offset, x-dist+offset, dist ] )
            res.append( [ y-offset, x-dist+offset, dist ] )
            res.append( [ y-dist+offset, x-offset, dist ] )
            res.append( [ y-dist+offset, x+offset, dist ] )
    res2 = []
    for r in res:
        if r not in res2:
            res2.append(r)
    return res2

def part1(raw):
    data = EX1[:]
    data = raw[:]
    grid = [list(line) for line in data]
    start = find_char(grid, "S")
    finish = find_char(grid, "E")
    grid[finish[0]][finish[1]] = "."
    # Generate path through race track
    path = [start]
    current = start
    while current != finish:
        y,x = current
        if grid[y-1][x] == "." and [y-1,x] not in path:
            current = [y-1,x]
            path.append(current)
        if grid[y+1][x] == "." and [y+1,x] not in path:
            current = [y+1,x]
            path.append(current)
        if grid[y][x-1] == "." and [y,x-1] not in path:
            current = [y,x-1]
            path.append(current)
        if grid[y][x+1] == "." and [y,x+1] not in path:
            current = [y,x+1]
            path.append(current)
    print(len(path),"==>",path)
    CHEAT_LENGTH = 2
    cheats = {}
    cheat_list = []
    for i,node in enumerate(path):
        y,x = node
        offsets = get_coords_of_manhattan_distance(node, 2)
        for offset in offsets:
            if offset in path[i+1:]:
                dist = path.index(offset)-i
                if dist > 2:
                    if [node,offset] not in cheat_list:
                        cheat_list.append([node,offset])
                        dist = dist-2
                        print(f"Cheat at pos {i} to jump {dist} from {node} to {offset}")
                        if dist not in cheats.keys():
                            cheats[dist] = 1
                        else:
                            cheats[dist] += 1
    pprint(cheats)
    over100 = 0
    for k,v in cheats.items():
        if k >= 100:
            over100 += v
    return over100

def part2(raw):
    data = EX1[:]
    #data = raw[:]
    grid = [list(line) for line in data]
    start = find_char(grid, "S")
    finish = find_char(grid, "E")
    grid[finish[0]][finish[1]] = "."
    # Generate path through race track
    path = [start]
    current = start
    while current != finish:
        y,x = current
        if grid[y-1][x] == "." and [y-1,x] not in path:
            current = [y-1,x]
            path.append(current)
        if grid[y+1][x] == "." and [y+1,x] not in path:
            current = [y+1,x]
            path.append(current)
        if grid[y][x-1] == "." and [y,x-1] not in path:
            current = [y,x-1]
            path.append(current)
        if grid[y][x+1] == "." and [y,x+1] not in path:
            current = [y,x+1]
            path.append(current)
    print(len(path),"==>",path)
    CHEAT_LENGTH = 20
    cheats = {}
    for i in range(100):
        cheats[i] = 0
    for i,node in enumerate(path):
        cheat_list = []
        print(f"{i}/{len(path)}")
        y,x = node
        offsets = get_coords_upto_manhattan_distance(node, CHEAT_LENGTH)
        for offset in offsets:
            y2, x2, dist_traversed_in_cheat = offset
            destination = [y2,x2]
            if destination in path[i+1:]:
                dist = path.index(destination)-i-dist_traversed_in_cheat
                if [node,offset] not in cheat_list:
                    cheat_list.append([node,offset])
                    #print(f"Cheat at pos {i} to jump {dist} from {node} to {offset}")
                    if dist not in cheats.keys():
                        cheats[dist] = 1
                    else:
                        cheats[dist] += 1
    over100 = 0
    for k,v in cheats.items():
        if k >= 50 and v > 0:
            print(f"{k}: {v}")
        if k >= 100:
            over100 += v
    return over100
    # 863106 too low

if __name__=="__main__":
    start = time.time()
    #result = part1(get_data())
    #print(f"Part 1 result:",result)
    result = part2(get_data())
    print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


