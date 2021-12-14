# Day 13
# 2d array reflections

# Parse data
with open("day13.txt", "r") as f:
    data = f.read().splitlines()

coords = []
instrs = []
maxx, maxy = 0,0
i = 0
while data[i] != "":
    coord = [int(m) for m in data[i].split(",")]
    coords.append(coord)
    maxx = max(maxx, coord[0])
    maxy = max(maxy, coord[1])
    i += 1
while i<len(data):
    if data[i][:11] == "fold along ":
        instr = data[i][11:].split("=")
        instrs.append((instr[0], int(instr[1])))
    i += 1
print(coords)
print(instrs)


def print_paper(paper):
    for row in paper:
        for char in row:
            print(char, end=" ")
        print()
    print()

def plot_points(paper, coords):
    for c in coords:
        paper[c[1]][c[0]] = '#'

def create_paper(x,y):
    return [['.' for i in range(0, x)] for j in range(0, y)]

# Let's go! Part 1 & 2

paper = create_paper(maxx+1, maxy+1)
plot_points(paper, coords)

for instr in instrs:
    xy, fold = instr
    if xy == 'y':
        paper2 = create_paper(len(paper[0]), fold)
        for y in range(0,fold):
            for x in range(0, len(paper[y])):
                if paper[y][x] == '#':
                    paper2[y][x] = paper[y][x]
                if paper[ fold*2 - y ][x] == '#':
                    paper2[y][x] = paper[ fold*2 - y ][x]
        paper = paper2
    elif xy == 'x':
        paper2 = create_paper(fold, len(paper))
        for x in range(0,fold):
            for y in range(0, len(paper)):
                if paper[y][x] == '#':
                    paper2[y][x] = paper[y][x]
                if paper[y][ fold*2 - x ] == '#':
                    paper2[y][x] = paper[y][ fold*2 - x ]
        paper = paper2
    dots = sum([row.count('#') for row in paper])
    print("Dots",dots)
print_paper(paper)
