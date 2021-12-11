
# Read file as 2d array of integers
with open("day11.txt", "r") as f:
    data = [[int(n) for n in row] for row in f.read().splitlines()]

def print_state(data, msg=""):
    if msg != "":
        print(msg)
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            print(data[y][x], end=" ")
        print()
    print()

def flash(data, row, col):
    flashes = 0
    # Valid position?
    if row >= 0 and row < len(data) and col >= 0 and col < len(data[row]):
        #print_state(data,f"flash for {row},{col} start")
        if data[row][col] > 0: # Haven't flashed yet, increase our energy level
            data[row][col] += 1
        if data[row][col] > 9: # flash!
            data[row][col] = 0
            # Part 2 hackery - if everything is zero terminate the program
            if sum( [ sum(n) for n in data ]) == 0:
                print("ALL FLASH!!")
                exit()
            flashes += 1
            flashes += flash(data, row-1, col-1) # top left
            flashes += flash(data, row-1, col) # top middle
            flashes += flash(data, row-1, col+1) # top right
            flashes += flash(data, row, col-1) # middle left
            flashes += flash(data, row, col+1) # middle right
            flashes += flash(data, row+1, col-1) # bottom left
            flashes += flash(data, row+1, col) # bottom right
            flashes += flash(data, row+1, col+1) # bottom middle
    return flashes

def step(data):
    flashes = 0
    # Increase energy levels by 1
    for row in range(0, len(data)):
        for col in range(0, len(data[row])):
            data[row][col] += 1
    # Energy > 9 results in a flash
    for row in range(0, len(data)):
        for col in range(0, len(data[row])):
            if data[row][col] > 9: # Flash
                flashes += flash(data, row, col)
    return flashes

def part1(data):
    flashes = 0
    print_state(data,"start")
    i = 1
    while i < 1000:
        print(f"starting step {i}")
        flashes += step(data)
        print_state(data,f"after step {i}")
        i += 1
    print(flashes)

part1(data)
