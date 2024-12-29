import math, random, numpy, os, re, copy, time

DEMO = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def show_grid(grid):
    print("   ",end="")
    for x in range(0, len(grid[0])):
        print(x % 10, end="")
    print()
    for y in range(len(grid)):
        print(f"{y:02} " + "".join(grid[y]))
    print()

def part1(raw):    
    data = DEMO[:]
    # data = raw[:]
    data = "\n".join(data)
    grid, moves = data.split("\n\n")
    grid = grid.splitlines()
    grid = [list(line) for line in grid]
    moves = moves.replace("\n", "")
    print("grid",grid)
    print("moves",moves)
    # Find robot
    robot = [0,0]
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "@":
                robot = [y,x]
                break
    # Apply moves
    show_grid(grid)
    for i,move in enumerate(moves):
        print(f"Processing move {i}/{len(moves)} being {move}")
        if move == "<": change = (0,-1)
        elif move == ">": change = (0, 1)
        elif move == "^": change = (-1, 0)
        elif move == "v": change = (1, 0)
        # Is it possible to move?
        movement_possible = False
        tmp = robot[:]
        while grid[tmp[0]][tmp[1]] != "#":
            tmp = [ tmp[0]+change[0], tmp[1]+change[1] ]
            if grid[tmp[0]][tmp[1]] == ".":
                movement_possible = True
                break
        if movement_possible:
            # Shuffle everything between location of tmp and robot 1 square
            while tmp != robot:
                #print(f"Moving piece {grid[ tmp[0]-change[0] ][ tmp[1]-change[1] ]} from {tmp[0]-change[0]},{tmp[1]-change[1]} to {tmp[0]},{tmp[1]}")
                grid[ tmp[0] ][ tmp[1] ] = grid[ tmp[0]-change[0] ][ tmp[1]-change[1] ]
                tmp = [ tmp[0]-change[0], tmp[1]-change[1] ]
                #show_grid(grid)
            grid[ tmp[0] ][ tmp[1] ] = "."
            robot = [ tmp[0]+change[0], tmp[1]+change[1] ] # Add back as tmp will be one movement too far
            #show_grid(grid)
    # Display grid
    if True:
        show_grid(grid)
    # Calculate value of boxes
    print("Calculating box coordinates")
    total = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "[":
                total += y*100 + x
    print(total)
    return total

def check_forward(grid, loc, dir):
    y,x = loc
    dy, dx = dir
    newy, newx = y+dy, x+dx
    if newy < 0 or newy >= len(grid) or newx < 0 or newx >= len(grid[y]):
        return False
    if grid[newy][newx] == "#":
        return False
    if grid[newy][newx] == ".":
        return True
    if grid[newy][newx] == "[":
        return check_forward(grid, (newy, newx), dir) and check_forward(grid, (newy, newx+1), dir)
    if grid[newy][newx] == "]":
        return check_forward(grid, (newy, newx), dir) and check_forward(grid, (newy, newx-1), dir)
    print(f"Error: Shouldn't be here. loc {loc} dir {dir}")
    show_grid(grid)
    return False

def move_forward(grid, loc, dir):
    print(f"Move forward loc {loc} dir {dir} shape {grid[loc[0]][loc[1]]}")
    to_move = []
    y,x = loc
    dy, dx = dir
    # Create a stack with all moves required
    to_move.append([y,x])
    moves_added = True
    while moves_added:
        moves_added = False
        for i in range(0, len(to_move)):
            y2,x2 = to_move[i][0]+dy, to_move[i][1]+dx
            if grid[y2][x2] == "[":
                if [y2,x2] not in to_move:
                    to_move.append([y2,x2])
                    moves_added = True
                if [y2,x2+1] not in to_move:
                    to_move.append([y2,x2+1])
                    moves_added = True
            if grid[y2][x2] == "]":
                if [y2,x2] not in to_move:
                    to_move.append([y2,x2])
                    moves_added = True
                if [y2,x2-1] not in to_move:
                    to_move.append([y2,x2-1])
                    moves_added = True
    # All required moves have been added, make the moves (in reverse order)
    for i in range(len(to_move)-1, -1, -1):
        y,x = to_move[i]
        newy, newx = y+dy, x+dx
        grid[newy][newx] = grid[y][x]
        grid[y][x] = "."

def part2(raw):
    data = raw[:]
    # data = DEMO[:]
    data = "\n".join(data)
    grid, moves = data.split("\n\n")
    grid = grid.splitlines()
    grid = [list(line) for line in grid]
    moves = moves.replace("\n", "")
    # Resize grid
    grid2 = []
    for y in range(0, len(grid)):
        row = []
        for x in range(0, len(grid[y])):
            if grid[y][x] == ".":
                row.append(".")
                row.append(".")
            if grid[y][x] == "O":
                row.append("[")
                row.append("]")
            if grid[y][x] == "@":
                row.append("@")
                row.append(".")
            if grid[y][x] == "#":
                row.append("#")
                row.append("#")
        grid2.append(row)
    grid = grid2[:]
    print("grid",grid)
    print("moves",moves)
    # Find robot
    robot = [0,0]
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "@":
                robot = [y,x]
                break
    # Apply moves
    show_grid(grid)
    for i,move in enumerate(moves):
        print(f"Processing move {i}/{len(moves)} being {move}")
        if move == "<": change = (0,-1)
        elif move == ">": change = (0, 1)
        elif move == "^": change = (-1, 0)
        elif move == "v": change = (1, 0)
        if move == "<" or move == ">":
            # Is it possible to move?
            movement_possible = False
            tmp = robot[:]
            while grid[tmp[0]][tmp[1]] != "#":
                tmp = [ tmp[0]+change[0], tmp[1]+change[1] ]
                if grid[tmp[0]][tmp[1]] == ".":
                    movement_possible = True
                    break
            if movement_possible:
                # Shuffle everything between location of tmp and robot 1 square
                while tmp != robot:
                    #print(f"Moving piece {grid[ tmp[0]-change[0] ][ tmp[1]-change[1] ]} from {tmp[0]-change[0]},{tmp[1]-change[1]} to {tmp[0]},{tmp[1]}")
                    grid[ tmp[0] ][ tmp[1] ] = grid[ tmp[0]-change[0] ][ tmp[1]-change[1] ]
                    tmp = [ tmp[0]-change[0], tmp[1]-change[1] ]
                grid[ tmp[0] ][ tmp[1] ] = "."
                robot = [ tmp[0]+change[0], tmp[1]+change[1] ] # Add back as tmp will be one movement too far
        else: # Vertical movement
            if check_forward(grid, robot, change):
                move_forward(grid, robot, change)
                grid[robot[0]][robot[1]] = "."
                robot = [ robot[0]+change[0], robot[1]+change[1] ]
        #if i == 35:
        #    exit()
        show_grid(grid)
    # Display grid
    if True:
        show_grid(grid)
    # Calculate value of boxes
    print("Calculating box coordinates")
    total = 0
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "[":
                total += y*100 + x
    print(total)

if __name__=="__main__":
    start = time.time()
    #result = part1(get_data())
    #print(f"Part 1 result:",result)
    #if result:
    result = part2(get_data())
    print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


