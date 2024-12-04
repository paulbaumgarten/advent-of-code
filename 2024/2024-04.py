import math, random, os, re
# import numpy as np

TEST = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

def xmas_check(data, y, x, dy, dx):
    y = y + dy
    x = x + dx
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return 0
    if data[y][x] != "M":
        return 0
    y = y + dy
    x = x + dx
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return 0
    if data[y][x] != "A":
        return 0
    y = y + dy
    x = x + dx
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return 0
    if data[y][x] != "S":
        return 0
    return 1

def part1(raw):
    data = raw
    data = [ list(line) for line in data ]
    xmas = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "X":
                xmas += xmas_check(data, y, x, 1, 1)
                xmas += xmas_check(data, y, x, 1, 0)
                xmas += xmas_check(data, y, x, 1, -1)
                xmas += xmas_check(data, y, x, 0, 1)
                xmas += xmas_check(data, y, x, 0, -1)
                xmas += xmas_check(data, y, x, -1, 1)
                xmas += xmas_check(data, y, x, -1, 0)
                xmas += xmas_check(data, y, x, -1, -1)
    return (xmas)

def xmas_check2(data, y, x):
    if y < 1 or y >= len(data)-1 or x < 1 or x >= len(data[y])-1:
        return 0
    if data[y-1][x-1] == "M" and data[y+1][x-1] == "M" and data[y-1][x+1] == "S" and data[y+1][x+1] == "S":
        return 1
    if data[y-1][x+1] == "M" and data[y+1][x+1] == "M" and data[y-1][x-1] == "S" and data[y+1][x-1] == "S":
        return 1
    if data[y-1][x-1] == "M" and data[y-1][x+1] == "M" and data[y+1][x-1] == "S" and data[y+1][x+1] == "S":
        return 1
    if data[y+1][x-1] == "M" and data[y+1][x+1] == "M" and data[y-1][x-1] == "S" and data[y-1][x+1] == "S":
        return 1
    return 0

def part2(raw):
    data = raw
    data = [ list(line) for line in data ]
    xmas = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == "A":
                xmas += xmas_check2(data, y, x)
    return (xmas)

if __name__=="__main__":
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)


