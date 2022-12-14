import time, math
from pprint import pprint
from PIL import Image

MAX_X = 1000
MAX_Y = 171

def draw_cave(data):
    img = Image.new("RGB", (MAX_X,MAX_Y))
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x]=="#":
                print((y,x))
                img.putpixel((x,y),(255,0,0))
            if data[y][x]=="+":
                print((y,x))
                img.putpixel((x,y),(0,255,0))
    img.show()

def plot_cave(data):
    cave = [['.' for x in range(MAX_X)] for y in range(MAX_Y)]
    # Plot cave
    for line in data:
        for c in range(len(line)-1):
            # Starting coordinate of a line is line[c], ending is line[c+1] inclusive
            dy = line[c+1][0] - line[c][0]
            dx = line[c+1][1] - line[c][1]
            if dx != 0 and dy != 0:
                print("Alarm - 2 directional change happening")
                exit()
            elif dx > 0 and dy == 0: # dx is change agent
                for x in range(0, dx+1):
                    cave[ line[c][0] ][ line[c][1] + x] = "#"
            elif dx < 0 and dy == 0: # dx is change agent
                for x in range(0, dx-1, -1):
                    cave[ line[c][0] ][ line[c][1] + x] = "#"
            elif dx == 0 and dy > 0: # dy is change agent
                for y in range(0, dy+1):
                    cave[ line[c][0] + y][ line[c][1] ] = "#"
            elif dx == 0 and dy < 0: # dy is change agent
                for y in range(0, dy-1, -1):
                    cave[ line[c][0] + y][ line[c][1] ] = "#"
    draw_cave(cave)
    return cave

def part1(data):
    cave = plot_cave(data)
    # Drop sand
    abyss = False
    grains = 0
    while not abyss:
        sy,sx = 0,500 # Sand location
        grains += 1
        print(grains)
        rest = False
        while (not rest) and (not abyss):
            if sy+1 >= len(cave):
                abyss = True
            elif cave[sy+1][sx] == ".":
                sy += 1
            elif sx>0 and cave[sy+1][sx-1] == ".": # Is down left available
                sy+=1
                sx-=1
            elif sx < len(cave[0]) and cave[sy+1][sx+1] == ".": # Is down left available
                sy+=1
                sx+=1
            else:
                cave[sy][sx] = "+"
                rest = True
    draw_cave(cave)
    return grains-1

def part2(data):
    cave = plot_cave(data)
    # Add new floor at y=170
    for x in range(0, len(cave[0])):
        cave[170][x] = "#"
    # Drop sand
    blocked = False
    grains = 0
    while not blocked:
        sy,sx = 0,500 # Sand location
        grains += 1
        print(grains)
        rest = False
        while (not rest) and (not blocked):
            if cave[sy+1][sx] == ".":
                sy += 1
            elif sx>0 and cave[sy+1][sx-1] == ".": # Is down left available
                sy+=1
                sx-=1
            elif sx < len(cave[0])-1 and cave[sy+1][sx+1] == ".": # Is down left available
                sy+=1
                sx+=1
            else:
                cave[sy][sx] = "+"
                rest = True
                if sy==0 and sx==500: blocked=True
    draw_cave(cave)
    return grains

def parse(filename):
    x1,y1,x2,y2=0,0,0,0
    with open(filename, "r") as f:
        data = f.read().splitlines()
    res = []
    for line in data:
        row = []
        coords = line.split(" -> ")
        for c in coords:
            x,y = c.split(",")
            x=int(x)
            y=int(y)
            row.append((y,x))
        res.append(row)
    return res

# Lower and upper bounds of the data for x 0 -> 541 and y 0 -> 168
start = time.time()
data = parse("./2022/day 14b.txt")
print(part1(data))
print(part2(data)) # Not 20166
print("Execution time:",time.time()-start)
