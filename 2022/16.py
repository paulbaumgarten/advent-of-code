import time, math
from pprint import pprint
from copy import copy
import itertools

class Valve:
    def __init__(self, id, flow, neighbors):
        self.id = id
        self.flow = flow
        self.neighbors = neighbors
    def __repr__(self) -> str:
        return f"Valve {self.id}, flow {self.flow}, neighbors {self.neighbors}"

max_pressure = 0
max_route = []
max_open = []
openable_valves = []
valves = {}

def visit_valve(valves, id, minutes_so_far, pressure_so_far, pressure_per_minute, route, open_valves):
    # journey AA DD CC BB AA II JJ II AA DD EE FF GG HH GG FF EE DD CC
    #print(f"Minute {minutes_so_far} visiting {id}")
    # No remaining valves to open
    if len(open_valves) >= openable_valves or minutes_so_far >= 29:
        global max_pressure, max_open, max_route
        pressure_total = pressure_so_far + (30-minutes_so_far)*pressure_per_minute
        if pressure_total > max_pressure:
            max_pressure = pressure_total
            max_open = copy(open_valves)
            max_route = copy(route)
            print(f"Route {route}. Status quo @ T{minutes_so_far} rate {pressure_per_minute} and total {pressure_so_far}. At T30, total released {pressure_total}")
        return
    # Move to valve 'id'
    minutes_so_far += 1
    pressure_so_far += pressure_per_minute
    # Visit the next valves without spending a minute to open this one
    for neighbor in valves[id].neighbors:
        new_route = copy(route)
        new_route.append(id)
        visit_valve(valves, neighbor, minutes_so_far, pressure_so_far, pressure_per_minute, new_route, open_valves)
    # Open valve 'id' if available
    if valves[id].flow > 0 and id not in open_valves:
        minutes_so_far += 1
        pressure_so_far += pressure_per_minute
        #if minutes_so_far >= 30:
        #    print(f"= Reached {id}. Minutes {minutes_so_far}. Pressure released {pressure_so_far}. Route {route}.")
        #    return 
        # Visit the next valves after spending a minute to open this one
        for neighbor in valves[id].neighbors:
            new_route = copy(route)
            new_route.append(id)
            new_open_list = copy(open_valves)
            new_open_list.append(id)
            visit_valve(valves, neighbor, minutes_so_far, pressure_so_far, pressure_per_minute+valves[id].flow, new_route, new_open_list)
    return

def dikstra(start, dest):
    to_visit = [ start ]
    closed = [ ]
    costs = { start: 0 }      # Zero cost to start
    routes = { start: [] }    # Zero jumps to start
    while len( to_visit ) > 0:
        # Find the item in the to_visit list with lowest cost, make it 'current'
        current = to_visit[0]
        for n in to_visit:
            if costs[n] < costs[current]:
                current = n
        # Remove 'current' from 'to_visit', add to 'closed_list'
        closed.append(current)
        to_visit.remove(current)
        # If current is destination, return cost/route
        if current == dest:
            return costs[current], routes[current]
        # Get the adjacent nodes for the current node
        adjacent_nodes = copy(valves[current].neighbors) # Build adjacent_nodes list
        # For all adjacent nodes
        for node in adjacent_nodes:
            # Calculate route from start to this adjacent node
            route_adj = copy(routes[current])
            route_adj.append(node)
            # Calculate cost from start to this adjacent node
            cost_adj = costs[current] + 1
            # If adjacent node is closed, continue (restart) loop
            if node in closed:
                continue
            # If adjacent node not in to_visit
            if node not in to_visit:
                # Add adjacent node to to_visit, costs, routes
                to_visit.append(node)
                costs[node] = cost_adj
                routes[node] = route_adj
            # Else if it is in to_visit
            else:
                # Calculate alternative cost via this route, if cost is lower this way, replace old cost
                if cost_adj < costs[node]:
                    costs[node] = cost_adj
                    routes[node] = route_adj
    # End of dikstra

def part1(data):
    # Calculate all possible shortest routes from AA to all possible openable_valves:
    routes = {}
    for i in range(0, len(openable_valves)):
        v2 = openable_valves[ i ]
        if v2 != 'AA':
            # Find route from v1 to v2
            cost, r = dikstra('AA',v2)
            print(f"Path from AA to {v2} is {r}")
            routes["AA-"+v2] = r
    # Calculate all possible shortest routes to visit all possible openable_valves:
    for i1 in range(0, len(openable_valves)-1):
        for i2 in range(1, len(openable_valves)):
            v1 = openable_valves[ i1 ]
            v2 = openable_valves[ i2 ]
            if v1 != v2:
                # Find route from v1 to v2
                print(f"Path from {v1} to {v2} is",end=" ")
                cost, r = dikstra(v1,v2)
                print(f"{r}")
                routes[v1+"-"+v2] = r
    # From AA, determine the various paths to all the possible sequences to visit all the openable_valves
    print("Openable valves")
    print(openable_valves)
    print("Generating permutations")
    progress = 0
    max_released = 0
    for path in itertools.permutations(openable_valves):
        # Calculate pressure released for each scenario
        progress += 1
        if progress % 1000000 == 0:
            print(progress // 1000000,"million of 1 300 000 million")
        t = 1
        per_minute = 0
        released = 0
        previous_n = 'AA'
        for n in path:
            # Move to n
            if previous_n+"-"+n in routes.keys():
                jumps = len(routes[previous_n+"-"+n])
            elif n+"-"+previous_n in routes.keys():
                jumps = len(routes[n+"-"+previous_n])
            else:
                print(f"key error n {n} previous_n {previous_n}")
                exit()
            t += jumps
            released = released + jumps * per_minute
            # Open valve for n
            t += 1
            released += per_minute
            # Indicate new per_minute for subsequent minutes
            per_minute += valves[n].flow
            previous_n = n
        while t <= 30:
            t += 1
            released += per_minute
        if released > max_released:
            print(f"path {path} released {released} {per_minute}")
            max_released = released
    return max_released

def part2(data):
    pass

def parse(filename):
    # Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    with open(filename, "r") as f:
        for line in f.read().splitlines():
            id = line[6:8]
            flow_rate = int(line[23:].split(";")[0])
            if flow_rate > 0:
                openable_valves.append(id)
            if line.find("lead to valves") > 0:
                neighbors = line[ line.find("lead to valves ")+15 : ].split(", ")
            else:
                neighbors = [line[ line.find("leads to valve ")+15 : ] ]
            valves[id] = Valve(id, flow_rate, neighbors)
    for k, datum in valves.items():
        print(datum)
    return None

start = time.time()
data = parse("./2022/day 16.txt")
print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)


"""
def dikstra(data, start, dest):
    to_visit = [ start ]
    closed = []
    costs = []
    routes = []
    while len( to_visit ) > 0:
        # Find the item in the to_visit list with lowest cost, make it 'current'
        current = to_visit[0]
        for n in to_visit:
            if cost[n] < cost[current]:
                current = n
        # Remove 'current' from 'to_visit', add to 'closed_list'
        closed.append(current)
        to_visit.remove(current)
        # If current is destination, return cost/route
        if current == dest:
            return costs[current], routes[current]
        # Get the adjacent nodes for the current node
        adjacent_nodes = []
        # Build adjacent_nodes list
        # For all adjacent nodes
            # Calculate route from start to this adjacent node
            # Calculate cost from start to this adjacent node
            # If adjacent node is closed, continue (restart) loop
            # If adjacent node not in to_visit
                # Add adjacent node to to_visit, costs, routes
            # Else if it is in to_visit
                # Calculate alternative cost via this route
                # If close is lower this way, replace old cost
    # End of dikstra
"""