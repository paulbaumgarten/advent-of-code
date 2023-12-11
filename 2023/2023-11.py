
FILE = "./2023/2023-11.txt"

TEST = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    # Expand the universe!
    data2 = []
    for y in range(0, len(data)):
        if data[y].count("#") == 0:
            data2.append(data[y])
            data2.append(data[y])
        else:
            data2.append(data[y])
    columns_to_insert = []
    for x in range(0, len(data2[0])):
        column = [data2[row][x] for row in range(0, len(data2))]
        if column.count("#") == 0:
            columns_to_insert.insert(0,x)
    for y in range(0, len(data2)):
        for c in columns_to_insert:
            data2[y] = data2[y][:c] + "." + data2[y][c:]
        print(data2[y])
    # Find all the points
    points = []
    for y in range(0, len(data2)):
        for x in range(0, len(data2[y])):
            if data2[y][x] == "#":
                points.append((y,x))
    # Find the sum between all pairs
    total = 0
    for p1 in range(0, len(points)):
        for p2 in range(p1+1, len(points)):
            distance = abs(points[p2][0]-points[p1][0]) + abs(points[p2][1]-points[p1][1])
            print(points[p1], points[p2], distance)
            total += distance
    print(total)

def get_distance(data, q, r):
    dist = 0
    y1 = min(q[0], r[0])
    y2 = max(q[0], r[0])
    x1 = min(q[1], r[1])
    x2 = max(q[1], r[1])

    for y in range(y1, y2):
        if data[y][q[1]] == "|":
            dist += 1000000
        elif data[y][q[1]] == "+":
            dist += 1000000
        else:
            dist += 1
    for x in range(x1, x2):
        if data[q[0]][x] == "-":
            dist += 1000000
        elif data[q[0]][x] == "+":
            dist += 1000000
        else:
            dist += 1
    return dist

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    # Expand the universe!
    data2 = []
    for y in range(0, len(data)):
        if data[y].count("#") == 0:
            data2.append(data[y].replace(".","|"))
        else:
            data2.append(data[y])
    columns_to_insert = []
    for x in range(0, len(data2[0])):
        column = [data2[row][x] for row in range(0, len(data2))]
        if column.count("#") == 0:
            columns_to_insert.insert(0,x)
    for y in range(0, len(data2)):
        for c in columns_to_insert:
            if data2[y][c] == ".":
                data2[y] = data2[y][:c] + "-" + data2[y][c+1:]
            else:
                data2[y] = data2[y][:c] + "+" + data2[y][c+1:]
        print(data2[y])
    # Find all the points
    points = []
    for y in range(0, len(data2)):
        for x in range(0, len(data2[y])):
            if data2[y][x] == "#":
                points.append((y,x))
    # Find the sum between all pairs
    total = 0
    for p1 in range(0, len(points)):
        for p2 in range(p1+1, len(points)):
            distance = get_distance(data2, points[p1], points[p2])
            print(points[p1], points[p2], distance)
            total += distance
    print(total)    
#part1()
part2()

