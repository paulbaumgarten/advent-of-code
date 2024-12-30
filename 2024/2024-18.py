import math, random, numpy, os, re, copy, time

EX="""5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def print_grid(grid):
    for y in range(0, len(grid)):
        print(" ".join(grid[y]))
    print()

def shortest_path(grid, start, finish):
    y,x = start
    q = [[y,x,0]]
    visited = [[y,x]]
    costs = []
    while len(q) > 0:
        y,x,cost = q.pop(0)
        if [y,x] == finish:
            costs.append(cost)
        else:
            if y > 0 and grid[y-1][x] == "." and (not [y-1,x] in visited):
                q.append( [y-1,x,cost+1] )
                visited.append( [y-1,x] )
            if y < len(grid)-1 and grid[y+1][x] == "." and (not [y+1,x] in visited):
                q.append( [y+1,x,cost+1] )
                visited.append( [y+1,x] )
            if x > 0 and grid[y][x-1] == "." and (not [y,x-1] in visited):
                q.append( [y,x-1,cost+1] )
                visited.append( [y,x-1] )
            if x < len(grid[0])-1 and grid[y][x+1] == "." and (not [y,x+1] in visited):
                q.append( [y,x+1,cost+1] )
                visited.append( [y,x+1] )
    print("Costs: ",costs)
    return costs

def part1(raw):
    BYTES_DOWN = 12
    SIZE = 7
    data = EX[:]
    if True: # Use real
        BYTES_DOWN = 1024
        SIZE = 71
        data = raw[:]
    coords = []
    for line in data:
        x,y = line.split(",")
        coords.append((int(y),int(x))) 
    # Start
    grid = [["." for x in range(SIZE)] for y in range(SIZE)]
    pos = [0,0]
    finish = [SIZE-1,SIZE-1]
    for block in range(BYTES_DOWN):
        grid[ coords[block][0] ][ coords[block][1] ] = "#"
    print_grid(grid)
    l = shortest_path(grid, pos, finish)
    print(min(l))
    return(min(l))

def part2(raw):
    BYTES_DOWN = 12
    SIZE = 7
    data = EX[:]
    if True: # Use real
        BYTES_DOWN = 1024
        SIZE = 71
        data = raw[:]
    coords = []
    for line in data:
        x,y = line.split(",")
        coords.append((int(y),int(x))) 
    # Start
    grid = [["." for x in range(SIZE)] for y in range(SIZE)]
    pos = [0,0]
    finish = [SIZE-1,SIZE-1]
    for block in range(BYTES_DOWN):
        grid[ coords[block][0] ][ coords[block][1] ] = "#"
    print_grid(grid)
    l = shortest_path(grid, pos, finish)
    for i in range(BYTES_DOWN, len(coords)):
        grid[ coords[i][0] ][ coords[i][1] ] = "#"
        l = shortest_path(grid, pos, finish)
        if len(l) == 0:
            print("No path available after this block:")
            print(f"{coords[i][1]},{coords[i][0]}")
            break
    return(l)

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


