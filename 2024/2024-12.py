import math, random, numpy, os, re, copy, time

DEMO = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".splitlines()

DEMO2 = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA""".splitlines()

DEMO3 = """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE""".splitlines()


def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def print_grid(data):
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            print(data[y][x], end="")
        print()
    print()

def garden_plot(data, starty, startx):
    plot = data[starty][startx]
    q = [(starty, startx)]
    area = 0
    peri = 0
    while len(q) > 0:
        y, x = q.pop(0)
        if data[y][x] != ".":
            data[y][x] = "."
            area += 1
            peri += 4
            #print("y",y,"x",x,"area",area, "peri",peri)
            #print_grid(data)
            if y > 0 and data[y-1][x]==plot:
                peri -= 2
                q.append((y-1,x))
            if y < len(data)-1 and data[y+1][x]==plot:
                peri -= 2
                q.append((y+1,x))
            if x > 0 and data[y][x-1]==plot:
                peri -= 2
                q.append((y,x-1))
            if x < len(data[y])-1 and data[y][x+1]==plot:
                peri -= 2
                q.append((y,x+1))
    return area, peri        

def get_point(data, y, x):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return "."
    else:
        return data[y][x]

def discount(data, starty, startx):
    plot = data[starty][startx]
    shape = [['.' for q in range(len(data[0]))] for p in range(len(data))]
    q = [(starty, startx)]
    area = 0
    peri = 0
    while len(q) > 0:
        y, x = q.pop(0)
        if data[y][x] != ".":
            data[y][x] = "."
            shape[y][x] = plot
            area += 1
            peri += 4
            #print("y",y,"x",x,"area",area, "peri",peri)
            #print_grid(data)
            if y > 0 and data[y-1][x]==plot:
                peri -= 2
                q.append((y-1,x))
            if y < len(data)-1 and data[y+1][x]==plot:
                peri -= 2
                q.append((y+1,x))
            if x > 0 and data[y][x-1]==plot:
                peri -= 2
                q.append((y,x-1))
            if x < len(data[y])-1 and data[y][x+1]==plot:
                peri -= 2
                q.append((y,x+1))
    
    data_for_sides = copy.deepcopy(shape)
    area = 0
    corners = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data_for_sides[y][x] == plot:
                area += 1
                if get_point(data_for_sides, y-1,x) != plot and get_point(data_for_sides, y,x-1) != plot:
                    #print("y",y,"x",x,"corner top left")
                    corners += 1
                if get_point(data_for_sides, y+1,x) != plot and get_point(data_for_sides, y,x-1) != plot:
                    #print("y",y,"x",x,"corner bottom left")
                    corners += 1
                if get_point(data_for_sides, y+1,x) != plot and get_point(data_for_sides, y,x+1) != plot:
                    #print("y",y,"x",x,"corner bottom right")
                    corners += 1
                if get_point(data_for_sides, y-1,x) != plot and get_point(data_for_sides, y,x+1) != plot:
                    #print("y",y,"x",x,"corner top right")
                    corners += 1

                if get_point(data_for_sides, y-1,x) == plot and get_point(data_for_sides, y,x-1) == plot and get_point(data_for_sides, y-1,x-1) != plot:
                    #print("y",y,"x",x,"corner top left")
                    corners += 1
                if get_point(data_for_sides, y+1,x) == plot and get_point(data_for_sides, y,x-1) == plot and get_point(data_for_sides, y+1,x-1) != plot:
                    #print("y",y,"x",x,"corner bottom left")
                    corners += 1
                if get_point(data_for_sides, y+1,x) == plot and get_point(data_for_sides, y,x+1) == plot and get_point(data_for_sides, y+1,x+1) != plot:
                    #print("y",y,"x",x,"corner bottom right")
                    corners += 1
                if get_point(data_for_sides, y-1,x) == plot and get_point(data_for_sides, y,x+1) == plot and get_point(data_for_sides, y-1,x+1) != plot:
                    #print("y",y,"x",x,"corner top right")
                    corners += 1
    sides = corners
    return area, sides

def part1(raw):
    data = DEMO[:]
    #data = raw[:]
    data = [list(line) for line in data]
    total = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] != ".":
                print(f"Calculating for plot {data[y][x]}...  ",end="")
                area, perimeter = garden_plot(data, y, x)
                print(f"Area; {area}, Perimeter: {perimeter}")
                total += area*perimeter
    return total

def part2(raw):
    data = DEMO3[:]
    data = raw[:]
    print_grid(data)
    #data = raw[:]
    data = [list(line) for line in data]
    total = 0
    plots = []
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] != ".":
                print(f"Calculating for plot {data[y][x]}...  ",end="")
                area, sides = discount(data, y, x)
                print(f"Area; {area}, Sides: {sides}")
                total += area*sides
    return total

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


