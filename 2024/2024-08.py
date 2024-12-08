import math, random, numpy, os, re, copy, time

### Helper functions

DEMO = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()

def is_in_bounds(grid, y, x):
    return (y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y]))

def traverse_matrix(grid, callable):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            callable(grid, y, x)

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def part1(raw):
    data = DEMO[:]
    data = raw[:]
    data = [list(line) for line in data]
    #antinodes = [[0 for x in range(len(data[0]))] for y in range(len(data))]
    # Find all the antennas and their types
    antennas = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != ".":
                antennas.append((y,x,data[y][x]))
    # For each pair of antennas of the same time, plot their antinodes
    antinodes = {}
    for i in range(len(antennas)):
        for j in range(i+1,len(antennas)):
            if i != j: # Not the same antenna
                if antennas[i][2] == antennas[j][2]: # Same type of antenna
                    x1,y1,type1 = antennas[i]
                    x2,y2,type2 = antennas[j]
                    dx = x2-x1
                    dy = y2-y1
                    # Anitnode in one direction
                    ax, ay = x1-dx, y1-dy
                    if ax >=0 and ay >= 0 and ax < len(data[0]) and ay < len(data):
                        antinodes[(ax,ay)] = type1
                    # Antinode in the other direction
                    ax, ay = x2+dx, y2+dy
                    if ax >=0 and ay >= 0 and ax < len(data[0]) and ay < len(data):
                        antinodes[(ax,ay)] = type1
    #print(antinodes) 
    return len(antinodes)
# 261 (right answer for someone else)
# 234 not right
# 222

def part2(raw):
    data = DEMO[:]
    data = raw[:]
    data = [list(line) for line in data]
    #antinodes = [[0 for x in range(len(data[0]))] for y in range(len(data))]
    # Find all the antennas and their types
    antennas = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] != ".":
                antennas.append((y,x,data[y][x]))
    # For each pair of antennas of the same time, plot their antinodes
    antinodes = {}
    for i in range(len(antennas)):
        for j in range(i+1,len(antennas)):
            if i != j: # Not the same antenna
                if antennas[i][2] == antennas[j][2]: # Same type of antenna
                    x1,y1,type1 = antennas[i]
                    x2,y2,type2 = antennas[j]
                    dx = x2-x1
                    dy = y2-y1
                    # Anitnode in one direction
                    ax, ay = x2-dx, y2-dy
                    while ax >=0 and ay >= 0 and ax < len(data[0]) and ay < len(data):
                        antinodes[(ax,ay)] = type1
                        ax, ay = ax-dx, ay-dy
                    # Antinode in the other direction
                    ax, ay = x1+dx, y1+dy
                    while ax >=0 and ay >= 0 and ax < len(data[0]) and ay < len(data):
                        antinodes[(ax,ay)] = type1
                        ax, ay = ax+dx, ay+dy
    #print(antinodes) 
    return len(antinodes)

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


