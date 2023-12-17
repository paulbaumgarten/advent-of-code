import math, random

FILE = "./2023/2023-17.txt"

TEST = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".splitlines()

def bfs(grid):
    min_heat_loss = math.inf
    min_path = ""
    loop = 0
    h = len(grid)
    w = len(grid[0])
    minimums = [[ math.inf for x in range(0,w)] for y in range(0,h)]
    q = [(0,0,0,0,1,0,"")] # y, x, direction (0 right, 1 down, 2 left, 3 up), heat-loss-so-far, consec-hops-this-dir, total-hops-so-far
    while len(q) > 0:
        loop +=1 
        if loop % 10000 == 0:
            print(f"Loop counter at {loop}, q size is {len(q)}, current min is {min_heat_loss}")

        lowest = 0
        for i in range(1, len(q)):
            if q[i][3] < q[lowest][3]:
                lowest = i
        #y,x,dir,loss,consec,hops,path = q.pop(lowest)
        y,x,dir,loss,consec,hops,path = q.pop()

        loss += grid[y][x]
        path += f"{y},{x} "
        if loss < minimums[y][x]:
            minimums[y][x] = loss
            if (y,x) == (h-1,w-1):
                if loss-grid[0][0] < min_heat_loss:
                    min_heat_loss = loss-grid[0][0]
                    min_path = path
                continue
            if dir==0: # Right
                if consec < 3 and x < w-1 and loss+grid[y][x+1] < minimums[y][x+1]:
                    q.append((y,x+1,dir,loss,consec+1,hops+1,path))
                if y > 0 and loss+grid[y-1][x] < minimums[y-1][x]:
                    q.append((y-1,x,3,loss,0,hops+1,path))
                if y < h-1 and loss+grid[y+1][x] < minimums[y+1][x]:
                    q.append((y+1,x,1,loss,0,hops+1,path))
            if dir==1: # Down
                if consec < 3 and y < h-1 and loss+grid[y+1][x] < minimums[y+1][x]:
                    q.append((y+1,x,dir,loss,consec+1,hops+1,path))
                if x > 0 and loss+grid[y][x-1] < minimums[y][x-1]:
                    q.append((y,x-1,2,loss,0,hops+1,path))
                if x < w-1 and loss+grid[y][x+1] < minimums[y][x+1]:
                    q.append((y,x+1,0,loss,0,hops+1,path))
            if dir==2: # Left
                if consec < 3 and x > 0 and loss+grid[y][x-1] < minimums[y][x-1]:
                    q.append((y,x-1,dir,loss,consec+1,hops+1,path))
                if y > 0 and loss+grid[y-1][x] < minimums[y-1][x]:
                    q.append((y-1,x,3,loss,0,hops+1,path))
                if y < h-1 and loss+grid[y+1][x] < minimums[y+1][x]:
                    q.append((y+1,x,1,loss,0,hops+1,path))
            if dir==3: # Up
                if consec < 3 and y > 0 and loss+grid[y-1][x] < minimums[y-1][x]:
                    q.append((y-1,x,dir,loss,consec+1,hops+1,path))
                if x > 0 and loss+grid[y][x-1] < minimums[y][x-1]:
                    q.append((y,x-1,2,loss,0,hops+1,path))
                if x < w-1 and loss+grid[y][x+1] < minimums[y][x+1]:
                    q.append((y,x+1,0,loss,0,hops+1,path))
    for y in range(0, h):
        for x in range(0, w):
            print(f"{grid[y][x]:3} {minimums[y][x]:3}  ",end="")
        print()
    print(min_heat_loss)
    print(min_path)


def calc_cost(costs, current, adj_node):
    cost = 0
    y1,x1,_ = current
    y2,x2,_ = adj_node
    if y1==y2:
        if x1<x2:
            for x in range(x1+1,x2+1):
                cost += costs[y1][x]
        else:
            for x in range(x1-1,x2-1,-1):
                cost += costs[y1][x]
    else:
        if y1<y2:
            for y in range(y1+1,y2+1):
                cost += costs[y][x1]
        else:
            for y in range(y1-1,y2-1,-1):
                cost += costs[y][x1]
    return cost


def dijkstra(nodes, edges):
    w = len(edges)
    h = len(edges[0])
    costs = {k:math.inf for k in nodes.keys()}
    routes = {k:[] for k in nodes.keys()}
    q = []
    q.append((0,0,0))
    q.append((0,0,1))
    costs[(0,0,0)] = 0
    routes[(0,0,0)] = []
    costs[(0,0,1)] = 0
    routes[(0,0,1)] = []
    while len(q) > 0:
        current = q[0]
        for n in q:
            if costs[n] < costs[current]:
                current = n
        q.remove(current)

        y,x,d = current
        if (y,x) == (h-1,w-1):
            return costs[current], routes[current]

        for adj_node in nodes[current]:
            adj_route = routes[current].copy()
            adj_route.append(adj_node)
            adj_cost = costs[current] + calc_cost(edges, current, adj_node)
            if adj_cost < costs[adj_node]:
                costs[adj_node] = adj_cost
                routes[adj_node] = adj_route
                if adj_node not in q:
                    q.append(adj_node)



def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    for y in range(0, len(data)):
        data[y] = list(data[y])
        for x in range(0, len(data[y])):
            data[y][x] = int(data[y][x])
    nodes = {}
    for y in range(0,len(data)):
        for x in range(0,len(data[y])):
            # From y,x move vertically
            neighbours_v = []
            for n in range(y-3,y+4):
                if n >= 0 and n < len(data) and n != y:
                    neighbours_v.append((n,x,0))
            # From y,x move horizontally
            neighbours_h = []
            for n in range(x-3,x+4):
                if n >= 0 and n < len(data[0]) and n != x:
                    neighbours_h.append((y,n,1))
            nodes[(y,x,1)] = neighbours_v
            nodes[(y,x,0)] = neighbours_h
    #for k,v in nodes.items():
    #    print(f"{k} = {v}")
    cost, route = dijkstra(nodes, data)
    print(route)
    print(cost)

# 750 too low
# 1383 too high
# 758 correct

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    for y in range(0, len(data)):
        data[y] = list(data[y])
        for x in range(0, len(data[y])):
            data[y][x] = int(data[y][x])
    nodes = {}
    for y in range(0,len(data)):
        for x in range(0,len(data[y])):
            # From y,x move vertically
            neighbours_v = []
            for n in range(y-10,y+11):
                if n >= 0 and n < len(data) and abs(n-y)>=4:
                    neighbours_v.append((n,x,0))
            # From y,x move horizontally
            neighbours_h = []
            for n in range(x-10,x+11):
                if n >= 0 and n < len(data[0]) and abs(n-x)>=4:
                    neighbours_h.append((y,n,1))
            nodes[(y,x,1)] = neighbours_v
            nodes[(y,x,0)] = neighbours_h
    #for k,v in nodes.items():
    #    print(f"{k} = {v}")
    cost, route = dijkstra(nodes, data)
    print(route)        # TEST DATA = 0,0 0,8 4,8 4,12 12,12 = 94
    print(cost)
    
#part1()
part2() # 895 too high, 892 correct

