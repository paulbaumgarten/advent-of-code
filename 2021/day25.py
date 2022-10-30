# Day 25

with open("day25.txt", "r") as f:
    data = [[ch for ch in line] for line in f.read().splitlines()]

def print_data(data):
    for row in data:
        for c in row:
            print(c,end=" ")
        print()
    print()

def part1(data):
    steps = 0
    movement = True
    while movement:
        print(steps)
        # print_data(data)
        # if steps == 60: break
        movement = False
        next = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
        # Apply horizontal movement
        for y in range(0, len(data)):
            for x in range(0, len(data[y])):
                if data[y][x] == '>': 
                    if data[y][(x+1) % len(data[y])] == '.':
                        next[y][(x+1) % len(data[y])] = '>'
                        movement = True
                    else:
                        next[y][x] = '>'
                if data[y][x] == 'v': next[y][x] = 'v'
        data = next
        next = [['.' for _ in range(len(data[0]))] for _ in range(len(data))]
        # Apply vertical movement
        for y in range(0, len(data)):
            for x in range(0, len(data[y])):
                if data[y][x] == 'v':
                    if data[(y+1) % len(data)][x] == '.':
                        next[(y+1) % len(data)][x] = 'v'
                        movement = True
                    else:
                        next[y][x] = 'v'
                if data[y][x] == '>': next[y][x] = '>'
        data = next
        steps += 1
    return steps

print(part1(data))

