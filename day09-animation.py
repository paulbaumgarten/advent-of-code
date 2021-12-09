
# Part 1
# - Find the low points
# - Risk value of low points = 1 + it's value
# - Sum of all risk values
# Test data = 15

"""
2199943210
3987894921
9856789892
8767896789
9899965678
"""

with open("day09.txt", "r") as f:
    data = f.read().splitlines()

minimums = []
for row in range(0, len(data)):
    for col in range(0, len(data[row])):
        above = int(data[row-1][col]) if row > 0 else 10
        below = int(data[row+1][col]) if row < len(data)-1 else 10
        left = int(data[row][col-1]) if col > 0 else 10
        right = int(data[row][col+1]) if col < len(data[row])-1 else 10
        here = int(data[row][col])
        if here < above and here < below and here < left and here < right and here < 9:
            minimums.append(int(here)+1)
            print(here," = ",above,below,left,right)
risk = sum(minimums)
print(risk) # 444

# Part 2
# Basin sizes - all multiplied together
# Test data = 1134

# Convert data into integers
d2 = [[int(ch) for ch in line] for line in data]
# print(d2)
import time

def draw(data):
    # Go to home
    print("\x1b[H;", end="")
    for y in range(0,60):
        for x in range(len(data[y])):
            if data[y][x] < 0:
                print(".", end="")
            else:
                print(data[y][x], end="")
        print("")
    time.sleep(0.01)

def get_basin_size(data, y, x):
    draw(data)
    if int(data[y][x]) >= 0 and int(data[y][x]) < 9:
        size = 1
        data[y][x] = -1
        if x > 0 and data[y][x-1] > -1 and data[y][x-1] < 9: # Go left
            size += get_basin_size(data, y, x-1)
        if x < len(data[y])-1 and data[y][x+1] > -1 and data[y][x+1] < 9: # Go right
            size += get_basin_size(data, y, x+1)
        if y > 0 and data[y-1][x] > -1 and data[y-1][x] < 9: # Go up
            size += get_basin_size(data, y-1, x)
        if y < len(data)-1 and data[y+1][x] > -1 and data[y+1][x] < 9: # Go down
            size += get_basin_size(data, y+1, x)
        return size
    else:
        return 0

basins = []
for row in range(0, len(d2)):
    for col in range(0, len(d2[row])):
        if d2[row][col] < 9 and d2[row][col] > 0:
            size = get_basin_size(d2, row, col)
            print("row",row,"col",col, "basin size",size)
            basins.append(size)

basins = sorted(basins, reverse=True)
answer = basins[0] * basins[1] * basins[2]
print(answer)

# Animation published at: https://www.youtube.com/watch?v=EdMKCRyBQhI

