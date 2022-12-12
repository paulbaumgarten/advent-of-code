import time, math
from pprint import pprint

# a = low, z =  high
# S = current location = height a
# E = best signal = height z
# climb at most 1 height per step, but any downward is ok

def dikstra(data, start, dest):
    data[start[0]][start[1]] = 'a'
    data[dest[0]][dest[1]] = 'z'
    open_nodes = []
    closed_nodes = []
    costs = [[math.inf for x in range(len(data[0]))] for y in range(len(data))]
    costs[start[0]][start[1]] = 0
    routes = [[ [] for x in range(len(data[0]))] for y in range(len(data))]
    print(f"Start is at {start}, destination is at {dest}")
    # Start dikstra
    open_nodes.append(start)
    while len(open_nodes) > 0:
        current = open_nodes[0] 
        for n in open_nodes:
            if costs[n[0]][n[1]] <= costs[current[0]][current[1]]:
                current = n
        closed_nodes.append(current)
        open_nodes.remove(current)
        if current == dest:
            return costs[current[0]][current[1]], routes[current[0]][current[1]]

        adjacent_nodes = []
        max_new_height = chr(ord(data[current[0]][current[1]])+1)
        if current[0] > 0 and data[current[0]-1][current[1]] <= max_new_height: 
            adjacent_nodes.append([current[0]-1, current[1]])
        if current[0] < len(data)-1 and data[current[0]+1][current[1]] <= max_new_height: 
            adjacent_nodes.append([current[0]+1, current[1]])
        if current[1] > 0 and data[current[0]][current[1]-1] <= max_new_height: 
            adjacent_nodes.append([current[0], current[1]-1])
        if current[1] < len(data[0])-1 and data[current[0]][current[1]+1] <= max_new_height: 
            adjacent_nodes.append([current[0], current[1]+1])

        for adjacent_node in adjacent_nodes:
            adjacent_route = routes[current[0]][current[1]].copy()
            adjacent_route.append(adjacent_node)
            adjacent_cost = costs[current[0]][current[1]] + 1
            if adjacent_node in closed_nodes:
                continue
            if adjacent_node in open_nodes:
                if costs[adjacent_node[0]][adjacent_node[1]] < adjacent_cost:
                    continue
                else:
                    costs[adjacent_node[0]][adjacent_node[1]] = adjacent_cost
                    routes[adjacent_node[0]][adjacent_node[1]] = adjacent_route
                    if adjacent_node not in open_nodes: 
                        open_nodes.append(adjacent_node)
            # Add to the open list for further exploration
            else:
                costs[adjacent_node[0]][adjacent_node[1]] = adjacent_cost
                routes[adjacent_node[0]][adjacent_node[1]] = adjacent_route
                if adjacent_node not in open_nodes: 
                    open_nodes.append(adjacent_node)
    # End of dikstra

def part1(data):
    # Find 'S' and 'E'
    start = [0,0]
    dest = [0,0]
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == 'S': start = [y,x]
            if data[y][x] == 'E': dest = [y,x]
    return dikstra(data, start, dest)

def part2(data):
    starts = []
    dest = []
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if data[y][x] == 'S' or data[y][x] == 'a':
                starts.append([y,x])
            if data[y][x] == 'E': dest = [y,x]
    steps = []
    for s in starts:
        print(f"Starting from {s}")
        res = dikstra(data, s, dest)
        if res != None:
            print(f"  {res[0]}")
            steps.append(res[0])
        else:
            print(f"   None")
    steps = sorted(steps)
    return steps

start = time.time()

def parse(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    return [[ch for ch in str] for str in data]

data = parse("./2022/day12b.txt")
print(part1(data))
data = parse("./2022/day12b.txt")
print(part2(data))
print("Execution time:",time.time()-start)




