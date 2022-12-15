import time, math
from pprint import pprint

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

class Line:
    def __init__(self):
        self.fragments = []
        self.flattened = False

    def add_fragment(self, start, stop):
        self.flattened = False
        self.fragments.append((start,stop))

    def flatten(self): # Combine all fragments where possible
        self.flattened = True
        merge = True
        while merge:
            merge = False
            for i in range(0, len(self.fragments)-1):
                j = i+1
                while j < len(self.fragments):
                    a1,a2 = self.fragments[i]
                    b1,b2 = self.fragments[j]
                    # if line aaaa****bbbb (where *** == both lines)
                    if a1 <= b1 and b1 <= a2 and a2 <= b2:
                        self.fragments[i] = (a1, b2)
                        self.fragments.pop(j)
                        merge = True
                    # if line bbbb****aaaa (where *** == both lines)
                    elif b1 <= a1 and a1 <= b2 and b2 <= a2:
                        self.fragments[i] = (b1, a2)
                        self.fragments.pop(j)
                        merge = True
                    # if line aaaa****aaaa (where *** == both lines)
                    elif a1 <= b1 and b2 <= a2:
                        self.fragments[i] = (a1, a2)
                        self.fragments.pop(j)
                        merge = True
                    # if line bbbb****bbbb (where *** == both lines)
                    elif b1 <= a1 and a2 <= b2:
                        self.fragments[i] = (b1, b2)
                        self.fragments.pop(j)
                        merge = True
                    else:
                        j += 1
                         
    def length(self): # Get length of flattened line     
        if not self.flattened:
            self.flatten()
        leng = 0
        for frag in self.fragments:
            leng = leng + frag[1] - frag[0]
        return leng

def part1(data, target):
    # List of sensors that will be relevant for the target row
    line = Line()
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
        line.add_fragment(data[i].x-horizontal_dist, data[i].x+horizontal_dist+1)
    # Count any beacons in the row to deduct
    line.flatten()
    hmm = sorted(line.fragments, key=lambda x: x[0])
    pprint(hmm)
    beacons_in_row = []
    for i in range(0, len(data)):
        if data[i].by==target and data[i].bx not in beacons_in_row:
            beacons_in_row.append(data[i].bx)
    return line.length() - len(beacons_in_row)

def part2(data, target):
    lower = 0
    upper = 4000000
    for y in range(lower,upper+1):
        line = Line()
        for i in range(0, len(data)):
            manhattan = abs(data[i].x - data[i].bx) + abs(data[i].y - data[i].by)
            data[i].manhattan = manhattan
            if data[i].y < y and data[i].y + manhattan < y:
                continue
            elif data[i].y > y and data[i].y - manhattan > y:
                continue
            diff = abs(y - data[i].y)
            horizontal_dist = abs(diff - manhattan)
            #print(f"Relevant sensor {i}: {data[i]} manhattan distance {manhattan} horizontal {horizontal_dist}. Filling {horizontal_dist*2} places.")
            line.add_fragment(data[i].x-horizontal_dist, data[i].x+horizontal_dist+1)
        # Count any beacons in the row to deduct
        line.flatten()
        if len(line.fragments) > 1 or line.fragments[0][0] > 0 or line.fragments[0][1] < upper:
            print(f"y={y}, fragments={line.fragments}")
            if len(line.fragments)==2:
                return (line.fragments[1][0]-1) * 4000000 + y
        if y % 100000 == 0:
            print(f"y={y} processed")
    return None

#print(2740279*4000000 + 2625406) # 10961118625406

start = time.time()
# Example data. y=10, 26 positions filled
# Input data. y=2000000
#data,target = parse_file("./2022/day15example.txt"), 10
data,target = parse_file("./2022/day15.txt"), 2000000
#print(part1(data, target))
print(part2(data, target))
print("Execution time:",time.time()-start)
