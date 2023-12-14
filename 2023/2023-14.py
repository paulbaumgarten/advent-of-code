import hashlib

FILE = "./2023/2023-14.txt"

TEST = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST

    for y in range(0, len(data)):
        data[y] = list(data[y])

    # Move rocks
    moved = True
    while moved:
        moved = False
        for y in range(0, len(data)-1):
            for x in range(0, len(data[0])):
                if data[y][x] == '.' and data[y+1][x] == 'O':
                    data[y][x] = 'O'
                    data[y+1][x] = '.'
                    moved = True
    for y in range(0, len(data)):
        print("".join(data[y]))
    # Calculate load
    total = 0
    for y in range(0, len(data)):
        rocks = data[y].count("O")
        total = total + rocks * (len(data)-y)
    print(total)

def cycle(data):
    # Move north
    moved = True
    while moved:
        moved = False
        for y in range(0, len(data)-1):
            for x in range(0, len(data[0])):
                if data[y][x] == '.' and data[y+1][x] == 'O':
                    data[y][x] = 'O'
                    data[y+1][x] = '.'
                    moved = True
    # Move west
    moved = True
    while moved:
        moved = False
        for y in range(0, len(data)):
            for x in range(0, len(data[0])-1):
                if data[y][x] == '.' and data[y][x+1] == 'O':
                    data[y][x] = 'O'
                    data[y][x+1] = '.'
                    moved = True
    # Move south
    moved = True
    while moved:
        moved = False
        for y in range(0, len(data)-1):
            for x in range(0, len(data[0])):
                if data[y+1][x] == '.' and data[y][x] == 'O':
                    data[y][x] = '.'
                    data[y+1][x] = 'O'
                    moved = True
    # Move east
    moved = True
    while moved:
        moved = False
        for y in range(0, len(data)):
            for x in range(0, len(data[0])-1):
                if data[y][x+1] == '.' and data[y][x] == 'O':
                    data[y][x] = '.'
                    data[y][x+1] = 'O'
                    moved = True

def print_grid(data):
    for y in range(0, len(data)):
        print("".join(data[y]))

def get_hash(data):
    s = ""
    for row in data:
        for cell in row:
            s += cell
    return str(hashlib.sha256(s.encode("utf-8")).hexdigest())

def calc_load(data):
    load = 0
    for y in range(0, len(data)):
        rocks = data[y].count("O")
        load = load + rocks * (len(data)-y)
    return load

def part2():
    # Parse data
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    for y in range(0, len(data)):
        data[y] = list(data[y])
    # Do solve
    cache = []
    loads = []
    repeat_offset = -1
    repeat_size = -1
    for i in range(0, 10000):
        cycle(data)
        #print_grid(data)
        h = get_hash(data)
        loads.append(calc_load(data))
        print(i,h,loads[len(loads)-1])
        if h in cache:
            print(f"Found a repeat! Hash for {i} is also at {cache.index(h)}.")
            repeat_offset = cache.index(h)
            repeat_size = i - cache.index(h)
            print(f"Repeat size: {repeat_size} repeat offset: {repeat_offset}")
            break
        cache.append(h)
    # Calculate load
    n = ((1000000000 - repeat_offset) % repeat_size) + repeat_offset -1
    print(loads[n])
    
#part1()
part2() # 99432 too low

