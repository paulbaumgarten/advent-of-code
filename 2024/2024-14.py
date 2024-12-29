import math, random, numpy, os, re, copy, time

DEMO = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

class Robot:
    def __init__(self, px, py, vx, vy, w, h):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.w = w
        self.h = h

    def move(self):
        self.px = (self.px + self.vx) % self.w
        self.py = (self.py + self.vy) % self.h

    def get_quadrant(self):
        vertical_mid = self.h // 2
        horizontal_mid = self.w // 2
        if self.px < horizontal_mid and self.py < vertical_mid:
            return 1
        elif self.px > horizontal_mid and self.py < vertical_mid:
            return 2
        elif self.px < horizontal_mid and self.py > vertical_mid:
            return 3
        elif self.px > horizontal_mid and self.py > vertical_mid:
            return 4
        return 0

def part1(raw):
    data = DEMO[:]
    map_size = {"w":11,"h":7}
    data = raw[:]
    map_size = {"w":101,"h":103}
    robots = []
    moves_required = 100
    for i,this_robot in enumerate(data):
        px,py,vx,vy = this_robot.replace("p=","").replace(" v=",",").split(",")
        px,py,vx,vy = int(px), int(py), int(vx), int(vy)
        print(px,py,vx,vy)
        robots.append( Robot(px,py,vx,vy, map_size["w"], map_size["h"]) )
    for m in range(0, moves_required):
        for r in range(0, len(robots)):
            robots[r].move()
    quadrants = [0,0,0,0,0]
    for r in range(0, len(robots)):
        quadrants[ robots[r].get_quadrant() ] += 1
    return quadrants[1]*quadrants[2]*quadrants[3]*quadrants[4]
    # 224438715
    
def part2(raw):
    pass

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


