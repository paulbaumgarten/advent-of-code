import time, math
from pprint import pprint

start = time.time()
with open("./2022/day8.txt", "r") as f:
    data = f.read().splitlines()

demo="""30373
25512
65332
33549
35390""".splitlines()

def part1(data):
    visible = 0
    # Trees on outside of grid
    visible += (len(data)-1)*2 + (len(data[0])-1)*2
    print(visible)
    # Trees inside grid
    for y in range(1, len(data)-1):
        for x in range(1, len(data[0])-1):
            height = int(data[y][x])
            left = True
            right = True
            up = True
            down = True
            # To the top
            for n in range(y-1,-1,-1):
                if int(data[n][x]) >= height:
                    up = False
            # To the left
            for n in range(x-1,-1,-1):
                if int(data[y][n]) >= height:
                    left = False
            # To the right
            for n in range(x+1,len(data[0])):
                if int(data[y][n]) >= height:
                    right = False
            # To the bottom
            for n in range(y+1,len(data)):
                if int(data[n][x]) >= height:
                    down = False
            if up or left or right or down:
                print(f"OK    - Tree at y{y}x{x}height{height}")
                visible += 1
    return visible

def part2(data):
    results = []
    # Trees inside grid
    for y in range(1, len(data)-1):
        for x in range(1, len(data[0])-1):
            height = int(data[y][x])
            left = 0
            right = 0
            up = 0
            down = 0
            # To the top
            for n in range(y-1,-1,-1):
                up += 1
                if int(data[n][x]) >= height:
                    break
            # To the left
            for n in range(x-1,-1,-1):
                left += 1
                if int(data[y][n]) >= height:
                    break
            # To the right
            for n in range(x+1,len(data[0])):
                right += 1
                if int(data[y][n]) >= height:
                    break
            # To the bottom
            for n in range(y+1,len(data)):
                down += 1
                if int(data[n][x]) >= height:
                    break
            scenic = up * down * left * right
            results.append(scenic)
            print(f"Tree at y{y}x{x}height{height} has scenic {scenic} using left {left} right {right} up {up} down {down}")
    return max(results)

#print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)
