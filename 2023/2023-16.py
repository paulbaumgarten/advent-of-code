
FILE = "./2023/2023-16.txt"

TEST = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....""".splitlines()

ENERGIZED = []
VISITED = [] # Right, Down, Left, Up

def traverse(data, inity=0, initx=0, initd=0):
    global VISITED, ENERGIZED
    h = len(data)
    w = len(data[0])
    beams = [[inity, initx, initd]]
    while len(beams)>0:
        #print("popping a beam")
        y,x,direction = beams.pop()
        while True:
            if y>=0 and y<h and x>=0 and x<w:
                ENERGIZED[y][x] = 1
            else:
                break
            ch = data[y][x]
            #print(f"y {y} x {x} direction {direction} ch {ch} len(beams) {len(beams)}")
            #for n in range(0,len(ENERGIZED)):
            #    print("   ","".join(data[n]),"  ","".join([str(n) for n in ENERGIZED[n]]))
            if VISITED[y][x][direction]==1: # Been here, done that
                break
            VISITED[y][x][direction]=1
            if ch==".":
                pass # keep going
            elif ch=="\\":
                if direction==0: direction=1
                elif direction==1: direction=0
                elif direction==2: direction=3
                else:
                    direction=2
            elif ch=="/":
                if direction==0: direction=3
                elif direction==1: direction=2
                elif direction==2: direction=1
                else:
                    direction=0
            elif ch=="-":
                if direction==1 or direction==3:
                    beams.append([y,x+1,0])
                    beams.append([y,x-1,2])
                    break
            elif ch=="|":
                if direction==0 or direction==2:
                    beams.append([y+1,x,1])
                    beams.append([y-1,x,3])
                    break
            if direction == 0: # Right
                if x < w-1:
                    x+=1
                else:
                    break
            elif direction == 1: # Down
                if y < h-1:
                    y+=1
                else:
                    break
            elif direction == 2: # Left
                if x > 0:
                    x-=1
                else:
                    break
            elif direction == 3: # Up
                if y > 0:
                    y-=1
                else:
                    break
            ch = data[y][x]

def part1():
    global VISITED, ENERGIZED
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    for y in range(0, len(data)):
        data[y] = list(data[y])
    h = len(data)
    w = len(data[0])
    ENERGIZED = [[ 0 for x in range(w)] for y in range(h) ]
    VISITED = [[ [0,0,0,0] for x in range(w)] for y in range(h) ]
    traverse(data)
    tot = 0
    for part in ENERGIZED:
        tot += sum(part)
        print("".join([str(n) for n in part]))
    print(tot)

def part2():
    global VISITED, ENERGIZED
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    for y in range(0, len(data)):
        data[y] = list(data[y])
    h = len(data)
    w = len(data[0])
    maxi = 0
    print("Left and right columns ",end="")
    for y in range(0, h):
        print(y,end=" ")
        # Left column, going right
        ENERGIZED = [[ 0 for x in range(w)] for y in range(h) ]
        VISITED = [[ [0,0,0,0] for x in range(w)] for y in range(h) ]
        traverse(data, y, 0, 0)
        tot = 0
        for part in ENERGIZED:
            tot += sum(part)
        if tot > maxi:
            maxi = tot
        # Right column, going left
        ENERGIZED = [[ 0 for x in range(w)] for y in range(h) ]
        VISITED = [[ [0,0,0,0] for x in range(w)] for y in range(h) ]
        traverse(data, y, w-1, 2)
        tot = 0
        for part in ENERGIZED:
            tot += sum(part)
        if tot > maxi:
            maxi = tot
    print()
    print("Top and bottom rows",end="")
    for x in range(0, w):
        print(x,end=" ")
        # Top row, going down
        ENERGIZED = [[ 0 for x in range(w)] for y in range(h) ]
        VISITED = [[ [0,0,0,0] for x in range(w)] for y in range(h) ]
        traverse(data, 0, x, 1)
        tot = 0
        for part in ENERGIZED:
            tot += sum(part)
        if tot > maxi:
            maxi = tot
        # Bottom row, going up
        ENERGIZED = [[ 0 for x in range(w)] for y in range(h) ]
        VISITED = [[ [0,0,0,0] for x in range(w)] for y in range(h) ]
        traverse(data, h-1, x, 3)
        tot = 0
        for part in ENERGIZED:
            tot += sum(part)
        if tot > maxi:
            maxi = tot
    print()
    print("Max energization",maxi)
    
#part1()
part2()

