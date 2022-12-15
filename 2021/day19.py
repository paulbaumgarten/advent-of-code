import time, math
from pprint import pprint

start = time.time()
with open("./2021/day19demo.txt", "r") as f:
    data = f.read().splitlines()

demo="""--- scanner 0 ---
0,2
4,1
3,3

--- scanner 1 ---
-1,-1
-5,0
-2,1
"""

scanners = []
world = [] # From perspective of scanner 0

class Beacon:
    def __init__(self, locn):
        self.x,self.y,self.z = locn

    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}] "

    def rotate(self, x=0, y=0, z=0, pivotx=0, pivoty=0, pivotz=0):
        # Only designed for angle increments of 90,180,270 to spin around one axis at a time.
        if z==90 and x==0 and y==0:
            xnew = (self.x-pivotx) * math.cos(math.radians(90)) - (self.y-pivoty) * math.sin(math.radians(90))
            ynew = (self.x-pivotx) * math.sin(math.radians(90)) - (self.y-pivoty) * math.cos(math.radians(90))
            self.x = pivotx+xnew
            self.y = pivoty+ynew
            return True
        return False

    def shift(self, dx=0, dy=0, dz=0):
        self.x += dx
        self.y += dy
        self.z += dz
        return True

class Scanner:
    def __init__(self, id):
        self.id = id
        self.beacons = []
    def add_beacon(self, locn):
        self.beacons.append(Beacon(locn))
    def __repr__(self) -> str:
        return f"Scanner {self.id} has {len(self.beacons)} beacons @ " + "".join([str(b) for b in self.beacons])

def part1(data):
    scanner = 0
    for line in data:
        if line[0:11] == "--- scanner":
            scanner = int(line[12:].split(" ")[0])
            scanners.append(Scanner(scanner))
            if scanner != len(scanners)-1:
                print("error scanner != len(scanners)-1")
                exit()
            #print(f"scanner {scanner}")
            #print(scanners[0])
        elif line.count(",") == 2:
            #print(line)
            coords = [int(n) for n in line.split(",")]
            s = scanners[scanner]
            s.add_beacon(coords)
    b = scanners[0].beacons[0]
    pprint(b)
    b.rotate(z=90,pivotx=400,pivoty=-584)
    pprint(b)
    return None

def part2(data):
    pass

part1(data)
part2(data)
print("Execution time:",time.time()-start)

"""
Scanners 0 and 1 have overlapping detection cubes; the 12 beacons they both detect (relative to scanner 0) are at the following coordinates:

-618,-824,-621
-537,-823,-458
-447,-329,318
404,-588,-901
544,-627,-890
528,-643,409
-661,-816,-575
390,-675,-793
423,-701,434
-345,-311,381
459,-707,401
-485,-357,347

The full list of beacons (relative to scanner 0) is:

-892,524,684
-876,649,763
-838,591,734
-789,900,-551
-739,-1745,668
-706,-3180,-659
-697,-3072,-689
-689,845,-530
-687,-1600,576
-661,-816,-575
-654,-3158,-753
-635,-1737,486
-631,-672,1502
-624,-1620,1868
-620,-3212,371
-618,-824,-621
-612,-1695,1788
-601,-1648,-643
-584,868,-557
-537,-823,-458
-532,-1715,1894
-518,-1681,-600
-499,-1607,-770
-485,-357,347
-470,-3283,303
-456,-621,1527
-447,-329,318
-430,-3130,366
-413,-627,1469
-345,-311,381
-36,-1284,1171
-27,-1108,-65
7,-33,-71
12,-2351,-103
26,-1119,1091
346,-2985,342
366,-3059,397
377,-2827,367
390,-675,-793
396,-1931,-563
404,-588,-901
408,-1815,803
423,-701,434
432,-2009,850
443,580,662
455,729,728
456,-540,1869
459,-707,401
465,-695,1988
474,580,667
496,-1584,1900
497,-1838,-617
527,-524,1933
528,-643,409
534,-1912,768
544,-627,-890
553,345,-567
564,392,-477
568,-2007,-577
605,-1665,1952
612,-1593,1893
630,319,-379
686,-3108,-505
776,-3184,-501
846,-3110,-434
1135,-1161,1235
1243,-1093,1063
1660,-552,429
1693,-557,386
1735,-437,1738
1749,-1800,1813
1772,-405,1572
1776,-675,371
1779,-442,1789
1780,-1548,337
1786,-1538,337
1847,-1591,415
1889,-1729,1762
1994,-1805,1792
In total, there are 79 beacons.

"""