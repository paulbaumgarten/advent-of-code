import math, random, numpy, os, re, copy, time

DEMO = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def find_start(data):
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == "S":
                return (y,x)
    return (None,None)

def traverse_map(map, start, steps_remaining):
    points = [start]
    for i in range(0, steps_remaining):
        print(f"Processing step {i} which contains {len(points)} points.")
        new_points = []
        for j in range(0, len(points)):
            y,x = points[j]
            if y > 0 and map[y-1][x] != "#":
                if (y-1,x) not in new_points:
                    new_points.append((y-1,x))
            if y < len(map)-1 and map[y+1][x] != "#":
                if (y+1,x) not in new_points:
                    new_points.append((y+1,x))
            if x > 0 and map[y][x-1] != "#":
                if (y,x-1) not in new_points:
                    new_points.append((y,x-1))
            if x < len(map[y])-1 and map[y][x+1] != "#":
                if (y,x+1) not in new_points:
                    new_points.append((y,x+1))
        points = copy.deepcopy(new_points)
    return points

def plot(data,locations):
    inf = ""
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            val = data[ y % len(data) ][ x % len(data[0]) ]
            if (y,x) in locations:
                val = "X"
            inf += val
        inf += "\n"
    #print(inf)
    return inf

def traverse_map2(map, start, steps_remaining):
    points = [start]
    prev = 0
    prev_plot1 = ""
    prev_plot2 = ""
    history = []
    for i in range(0, steps_remaining):
        print(f"Processing step {i} which contains {len(points)} points.")
        history.append(len(points))
        new_points = []
        for j in range(0, len(points)):
            y,x = points[j]
            #print(f"y {y}, x {x}, mapy {mapy}, mapx {mapx}")
            if map[(y-1) % len(map)][x  % len(map[0])] != "#":
                if (y-1,x) not in new_points:
                    new_points.append((y-1,x))
            if map[(y+1) % len(map)][x % len(map[0])] != "#":
                if (y+1,x) not in new_points:
                    new_points.append((y+1,x))
            if map[y % len(map)][(x-1) % len(map[0])] != "#":
                if (y,x-1) not in new_points:
                    new_points.append((y,x-1))
            if map[y % len(map)][(x+1) % len(map[0])] != "#":
                if (y,x+1) not in new_points:
                    new_points.append((y,x+1))
        points = copy.deepcopy(new_points)
        #this_plot = plot(map, points)
    return points, history

def part1(raw):
    data = DEMO[:]
    data = raw[:]
    data = [list(line) for line in data]
    start = find_start(data)
    locations = traverse_map(data, start, 64)
    print(len(locations))
    return len(locations)

def part2(raw):
    data = DEMO[:]
    #data = raw[:]
    data = [list(line) for line in data]
    start = find_start(data)
    locations, history = traverse_map2(data, start, 70)
    print(len(locations))
    print(history)
    diffs = history[:]
    for g in range(10):
        new_diff = []
        for x in range(1, len(diffs)):
            new_diff.append(diffs[x]-diffs[x-1])
        print(g," ==> ",new_diff)
        diffs = new_diff[:]

if __name__=="__main__":
    start = time.time()
    #result = part1(get_data())
    #print(f"Part 1 result:",result)
    #if result:
    result = part2(get_data())
    print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


