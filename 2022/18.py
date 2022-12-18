import time, math
from pprint import pprint

class Cube:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.x1=True
        self.x2=True
        self.y1=True
        self.y2=True
        self.z1=True
        self.z2=True
        self.sides = self.x1+self.x2+self.y1+self.y2+self.z1+self.z2

    def update(self):
        self.sides = self.x1+self.x2+self.y1+self.y2+self.z1+self.z2

cubes = []

def part1(data):
    for i in range(0,len(data)):
        x,y,z=data[i].split(",")
        x=int(x)
        y=int(y)
        z=int(z)
        cubes.append(Cube(x,y,z))
    sides = 0
    for i in range(0, len(cubes)-1):
        for j in range(i, len(cubes)):
            if cubes[i].x==cubes[j].x and cubes[i].y==cubes[j].y and cubes[i].z+1==cubes[j].z:
                cubes[i].z2=False
                cubes[j].z1=False
                cubes[i].update()
                cubes[j].update()
            if cubes[i].x==cubes[j].x and cubes[i].y==cubes[j].y and cubes[i].z-1==cubes[j].z:
                cubes[i].z1=False
                cubes[j].z2=False
                cubes[i].update()
                cubes[j].update()
            if cubes[i].x==cubes[j].x and cubes[i].y+1==cubes[j].y and cubes[i].z==cubes[j].z:
                cubes[i].y2=False
                cubes[j].y1=False
                cubes[i].update()
                cubes[j].update()
            if cubes[i].x==cubes[j].x and cubes[i].y-1==cubes[j].y and cubes[i].z==cubes[j].z:
                cubes[i].y1=False
                cubes[j].y2=False
                cubes[i].update()
                cubes[j].update()
            if cubes[i].x+1==cubes[j].x and cubes[i].y==cubes[j].y and cubes[i].z==cubes[j].z:
                cubes[i].x2=False
                cubes[j].x1=False
                cubes[i].update()
                cubes[j].update()
            if cubes[i].x-1==cubes[j].x and cubes[i].y==cubes[j].y and cubes[i].z==cubes[j].z:
                cubes[i].x1=False
                cubes[j].x2=False
                cubes[i].update()
                cubes[j].update()
        sides += cubes[i].sides
    sides += cubes[len(cubes)-1].sides
    return sides


def part2(data):
    air = [[[0 for x in range(20)] for y in range(20)] for z in range(20)]
    for i in range(0,len(data)):
        x,y,z=data[i].split(",")
        x=int(x)
        y=int(y)
        z=int(z)
        air[z][y][x] = 1
    for z in range(20):
        for y in range(20):
            for z in range(20):
                # for all 8000 locations, can they reach the edge, or are they trapped?
                

def parse(filename):
    with open(filename, "r") as f:
        data = f.read().splitlines()
    return data

start = time.time()
data = parse("./2022/day 18 input.txt")
print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)
