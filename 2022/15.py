import time, math
from pprint import pprint

class Sensor:
    x=0
    y=0
    bx=0
    by=0
    def __init__(self,x,y,bx,by):
        self.x=x
        self.y=y
        self.bx=bx
        self.by=by
    def __repr__(self) -> str:
        return f"Sensor at x={self.x}, y={self.y}: closest beacon is at x={self.bx}, y={self.by}"

def part1(data, target):
    # List of sensors that will be relevant for the target row
    row = []
    for i in range(0, len(data)):
        print(data[i])
        manhattan = abs(data[i].x - data[i].bx) + abs(data[i].y - data[i].by)
        data[i].manhattan = manhattan
        if data[i].y < target and data[i].y + manhattan < target:
            continue
        elif data[i].y > target and data[i].y - manhattan > target:
            continue
        diff = abs(target - data[i].y)
        horizontal_dist = abs(diff - manhattan)
        print(f"Relevant sensor {i}: {data[i]} manhattan distance {manhattan} horizontal {horizontal_dist}. Filling {horizontal_dist*2} places.")
        for x in range(data[i].x-horizontal_dist, data[i].x+horizontal_dist+1, 1):
            if x not in row:
                row.append(x)
    # Delete any beacons in the list
    for i in range(0, len(data)):
        if data[i].by==target and data[i].bx in row:
            row.remove(data[i].bx)
    return len(row)

def part2(data):
    pass

def parse_file(filename):
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    with open(filename, "r") as f:
        data = f.read().splitlines()
    sensors = []
    for line in data:
        if not line.startswith("Sensor at x"):
            print("Data parsing error!")
            exit()
        words = line.split(" ")
        try:
            x = int(words[2][2:-1])
            y = int(words[3][2:-1])
            bx = int(words[8][2:-1])
            by = int(words[9][2:])
            sensors.append(Sensor(x,y,bx,by))
        except:
            print(f"Parse error: {line}")
    return sensors

start = time.time()
data = parse_file("./2022/day15.txt")
# Example data. y=10, 26 positions filled
# Input data. y=2000000
print(part1(data, 10))
print(part2(data))
print("Execution time:",time.time()-start)
