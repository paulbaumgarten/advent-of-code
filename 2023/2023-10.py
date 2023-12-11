
FILE = "./2023/2023-10.txt"

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

TEST = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".splitlines()

TEST2 = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".splitlines()

TEST3 = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........""".splitlines()

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    # Convert into 2D array of char
    for i in range(0, len(data)):
        data[i] = list(data[i])
    # Find the start
    start = None
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == 'S':
                start = [y,x]
                break
    # Do a lap
    over = False
    current = [start[0]+1,start[1]]
    moves = 1
    direction = "down"
    while not over:
        print("current",current,"driection",direction,"piece",data[current[0]][current[1]])
        match data[current[0]][current[1]]:
            case 'S': current[0] += 1
            case '|':
                if direction=="up": 
                    current[0] -= 1
                    direction = "up"
                else:
                    current[0] += 1
                    direction = "down"
            case '-':
                if direction=="left":
                    current[1] -= 1
                    direction = "left"
                else:
                    current[1] += 1
                    direction = "right"
            case 'L':
                if direction=="down":
                    current[1] += 1 # Move right
                    direction = "right"
                else:
                    current[0] -= 1 # Move up
                    direction = "up"
            case '7':
                if direction=="right":
                    current[0] += 1 
                    direction = "down"
                else:
                    current[1] -= 1
                    direction = "left"
            case 'F':
                if direction=="left":
                    current[0] += 1 
                    direction = "down"
                else:
                    current[1] += 1 
                    direction = "right"
            case 'J':
                if direction=="right":
                    current[0] -= 1
                    direction = "up"
                else:
                    current[1] -= 1
                    direction = "left"
            case _:
                print("ERROR")
        moves += 1
        #if moves > 10:
        #    break
        if data[current[0]][current[1]] == 'S':
            over = True
    print(moves, "most furtherest point is ",moves//2)
    

def draw_truth(visit):
    for y in range(0, len(visit)):
        for x in range(0, len(visit[y])):
            if not visit[y][x]:
                print(".",end="")
            else:
                print("T",end="")
        print("")

def flood(data, y,x, targets, symbol, debug=False):
    move = 0
    q = []
    q.append((y,x))
    while len(q) > 0:
        y,x = q.pop()
        if x < len(data[y])-1 and data[y][x+1] in targets:
            print("R",end="")
            data[y][x+1] = symbol
            q.append((y,x+1))
        if x > 0 and data[y][x-1]  in targets:
            print("L",end="")
            data[y][x-1] = symbol
            q.append((y,x-1))
        if y < len(data)-1 and data[y+1][x]  in targets:
            print("D",end="")
            data[y+1][x] = symbol
            q.append((y+1,x))
        if y > 0 and data[y-1][x]  in targets:
            print("U",end="")
            data[y-1][x] = symbol
            q.append((y-1,x))
        move += 1
        if debug and (move % 100 == 0):
            for y in range(0, len(data)):
                print("".join(data[y]))
            print()        
    return

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST3
    # Convert into 2D array of char
    for i in range(0, len(data)):
        data[i] = list(data[i])
    # Find the start
    start = None
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == 'S':
                start = [y,x]
                break
    # Do a lap
    over = False
    current = [start[0]+1,start[1]]
    moves = 1
    direction = "down"
    visit = [[False for n in range(0, len(data[y]))] for y in range(0,len(data))]
    visit[start[0]][start[1]] = True
    visit[start[0]+1][start[1]] = True
    while not over:
        print("current",current,"driection",direction,"piece",data[current[0]][current[1]])
        match data[current[0]][current[1]]:
            case 'S': 
                current[0] += 1
            case '|':
                if direction=="up": 
                    current[0] -= 1
                    direction = "up"
                else:
                    current[0] += 1
                    direction = "down"
            case '-':
                if direction=="left":
                    current[1] -= 1
                    direction = "left"
                else:
                    current[1] += 1
                    direction = "right"
            case 'L':
                if direction=="down":
                    current[1] += 1 # Move right
                    direction = "right"
                else:
                    current[0] -= 1 # Move up
                    direction = "up"
            case '7':
                if direction=="right":
                    current[0] += 1 
                    direction = "down"
                else:
                    current[1] -= 1
                    direction = "left"
            case 'F':
                if direction=="left":
                    current[0] += 1 
                    direction = "down"
                else:
                    current[1] += 1 
                    direction = "right"
            case 'J':
                if direction=="right":
                    current[0] -= 1
                    direction = "up"
                else:
                    current[1] -= 1
                    direction = "left"
            case _:
                print("ERROR")
        moves += 1
        visit[current[0]][current[1]] = True
        #draw_truth(visit)
        #if moves > 10:
        #    break
        if data[current[0]][current[1]] == 'S':
            over = True
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if not visit[y][x]:
                data[y][x] = '*'
        print("".join(data[y]))
    print()
    draw_truth(visit)
    # Flood fill the outer region
    flood(data, 0,0, ['*'], '.')
    print()
    for y in range(0, len(data)):
        print("".join(data[y]))
    print()
    # mega map time!
    mega = [['.' for x in range(0, len(data[0])*3)] for y in range(0,len(data)*3)]
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x] == "S":
                mega[y*3][x*3+0] = "S"
                mega[y*3][x*3+1] = "S"
                mega[y*3][x*3+2] = "S"
                mega[y*3+1][x*3+0] = "S"
                mega[y*3+1][x*3+1] = "S"
                mega[y*3+1][x*3+2] = "S"
                mega[y*3+2][x*3+0] = "S"
                mega[y*3+2][x*3+1] = "S"
                mega[y*3+2][x*3+2] = "S"
            if data[y][x] == "*":
                mega[y*3+1][x*3+1] = "*"
            if data[y][x] == "-":
                mega[y*3+1][x*3] = "#"
                mega[y*3+1][x*3+1] = "#"
                mega[y*3+1][x*3+2] = "#"
            if data[y][x] == "|":
                mega[y*3][x*3+1] = "#"
                mega[y*3+1][x*3+1] = "#"
                mega[y*3+2][x*3+1] = "#"
            if data[y][x] == "L":
                mega[y*3][x*3+1] = "#"
                mega[y*3+1][x*3+1] = "#"
                mega[y*3+1][x*3+2] = "#"
            if data[y][x] == "J":
                mega[y*3][x*3+1] = "#"
                mega[y*3+1][x*3+1] = "#"
                mega[y*3+1][x*3] = "#"
            if data[y][x] == "7":
                mega[y*3+1][x*3] = "#"
                mega[y*3+1][x*3+1] = "#"
                mega[y*3+2][x*3+1] = "#"
            if data[y][x] == "F":
                mega[y*3+1][x*3+2] = "#"
                mega[y*3+1][x*3+1] = "#"
                mega[y*3+2][x*3+1] = "#"

    print()
    flood(mega, 0,0, ['.'], ' ')
    flood(mega, 0,0, [' ',"*"], '!', False)

    print()
    for y in range(0, len(mega)):
        print("".join(mega[y]))
    print()

    stars = 0
    for y in range(0, len(mega)):
        for x in range(0, len(mega[y])):
            if mega[y][x] == "*":
                stars += 1
    print(stars)

#part1()
part2() # 0 766 775 525

