# Day 15
# Dijkstra pathfinding

import time, math

with open("day15.txt", "r") as f:
    data = f.read().splitlines()

grid = [[int(n) for n in line] for line in data]

def print_grid(grid):
    for row in grid:
        for n in row:
            print(f"{n:1}",end=" ")
        print()
    print()

class Node:
    def __init__(self, position, cost, cost_to_me):
        self.x = position[1]
        self.y = position[0]
        self.cost = cost # cost: of this node individually
        self.cost_to_me = cost_to_me # cost: from start, up to but not including this node 
        self.visited = False
    def __str__(self):
        return f"Node({self.y},{self.x}:{self.cost})"
    def get_total_cost(self):
        return self.cost_to_me + self.cost

def print_node_total_costs(nodes):
    for row in nodes:
        for n in row:
            print(f"{n.cost_to_me:2}+{n.cost:1}",end="  ")
        print()
    print()

def find_path(grid, start, target):
    # Create a set of unvisited nodes
    nodes = [[Node((y,x),grid[y][x],math.inf) for x in range(len(grid[0]))] for y in range(len(grid))]
    current = nodes[start[0]][start[1]]
    current.cost = 0 # Starting location has zero cost to get to 
    current.cost_to_me = 0 # Starting location has zero cost to get to 
    # adjacent_deltas = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    adjacent_deltas = [(-1,0), (0,-1), (0,1), (1,0)] # We can't move diagonally
    visit = [(start[0], start[1])]
    # While we haven't found our objective
    while len(visit) > 0 and current != target:
        next_to_visit = visit.pop(0)
        current = nodes[next_to_visit[0]][next_to_visit[1]]
        current.visited = True
        cost_to_parent = current.cost_to_me + current.cost
        # Try each of the 6 adjacent locations
        for delta in adjacent_deltas:
            y = next_to_visit[0] + delta[0]
            x = next_to_visit[1] + delta[1]
            # Is this location valid?
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                continue # Skip this - it's an invalid location
            possible = nodes[y][x]
            # If we've been here before check this is the more efficient solution before adding it to the visit list
            if (not possible.visited) or (possible.cost_to_me > cost_to_parent):
                possible.cost_to_me = cost_to_parent # We found a cheaper way to reach this possible.
                possible.visited = True
                visit.append((possible.y,possible.x))
    # print_node_total_costs(nodes)
    return nodes[target[0]][target[1]].cost_to_me + nodes[target[0]][target[1]].cost

### PART 1

# print_grid(grid)
# path = find_path(grid, [0,0], [9,9]) # Part 1 test
# path = find_path(grid, [0,0], [99,99]) # Part 1 actual
# print(path)

### PART 2

# Part 2 build the super grid - not the most efficient but it'll do i'm getting tired ;)
super_grid = []
for j in range(0,5):
    for y in range(0,len(grid)):
        row = []
        for i in range(0,5):
            for x in range(0,len(grid[0])):
                val = ((grid[y][x] - 1 + i + j) % 9) + 1
                row.append(val)
        super_grid.append(row)

# print_grid(super_grid) # check it works
# path = find_path(super_grid, [0,0], [49,49]) # Part 2 test
path = find_path(super_grid, [0,0], [499,499]) # Part 2 actual
print(path)
