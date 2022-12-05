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
beacons = {}
world = [] # From perspective of scanner 0

def part1(data):
    scanner = 0
    for line in data:
        if line[0:11] == "--- scanner":
            scanner = int(line[12:].split(" ")[0])
            scanners.append([])
            if scanner != len(scanners)-1:
                print("error scanner != len(scanners)-1")
                exit()
            print(f"scanner {scanner}")
        elif line.count(",") == 2:
            print(line)
            coords = [int(n) for n in line.split(",")]
            scanners[scanner].append(coords)
    pprint(scanners)
    # For every pair of beacons from scanner 1, see if any other scanners have that pair
    matches = 0
    for s1 in range(0,len(scanners)):
        for b1 in range(len(scanners[s1])): # beacons within scanner
            for b2 in range(b1+1, len(scanners[s1])): # beacons within scanner
                x1,y1,z1 = scanners[s1][b1]
                x2,y2,z2 = scanners[s1][b2]
                diff = (abs(x1-x2)**2+abs(y1-y2)**2+abs(z1-z2)**2)
                for s2 in range(s1+1,len(scanners)):
                    for b3 in range(len(scanners[s2])): # beacons within scanner
                        for b4 in range(b3+1, len(scanners[s2])): # beacons within scanner
                            x3,y3,z3 = scanners[s2][b3]
                            x4,y4,z4 = scanners[s2][b4]
                            diff2 = (abs(x3-x4)**2+abs(y3-y4)**2+abs(z3-z4)**2)
                            if diff==diff2: # or \
                                matches += 1
                                print(f"Scanner {s1} beacon {b1} and {b2} are {diff} distance apart")
                                print(f" -> possible match with Scanner {s2} beacon {b3} and {b4} are {diff2}")
                                groupdiff = diff
                                if groupdiff not in beacons.keys():
                                    beacons[groupdiff] = []
                                if (s1,b1,b2,scanners[s1][b1],scanners[s1][b2]) not in beacons[groupdiff]:
                                    beacons[groupdiff].append((s1,b1,b2,scanners[s1][b1],scanners[s1][b2]))
                                if (s2,b3,b4,scanners[s2][b3],scanners[s2][b4]) not in beacons[groupdiff]:
                                    beacons[groupdiff].append((s2,b3,b4,scanners[s2][b3],scanners[s2][b4]))
    print(f"Possible matches: {matches}")
    for x in beacons.keys():
        print(x, beacons[x])
    print(len(beacons.keys()))
    # Add scanner 0 to the world
    for beacon in scanners[0]:
        world.append(beacon)
    for match,beaconsets in beacons.items():
        item1 = beaconsets[0]
        for i in range(1, len(beaconsets)):
            item2 = beaconsets[1]
            # Scanner#, beacon signal # relative to the scanner x2, location xyz relative to the scanner x2
            scan1, sig1a, sig1b, loc1a, loc1b = item1
            scan2, sig2a, sig2b, loc2a, loc2b = item2
            # Determine orientation
            dx1 = abs(loc1a[0]-loc1b[0])
            dy1 = abs(loc1a[1]-loc1b[1])
            dz1 = abs(loc1a[2]-loc1b[2])
            dx2 = abs(loc2a[0]-loc2b[0])
            dy2 = abs(loc2a[1]-loc2b[1])
            dz2 = abs(loc2a[2]-loc2b[2])
            if dx1==dx2 and dy1==dy2 and dz1==dz2:
                print(f"orientation of scanners {scan1} x/y/z stays   {scan2} x/y/z")
                print(loc1a, loc1b, loc2a, loc2b)
                offsetx = loc1a[0]-loc2a[0]
                offsetx2 = loc1b[0]-loc2b[0]
                if offsetx != offsetx2:
                    offsetx = loc1a[0]-loc2b[0]
                    offsetx2 = loc1b[0]-loc2a[0]
                offsety = loc1a[1]-loc2a[1]
                offsety2 = loc1b[1]-loc2b[1]
                if offsety != offsety2:
                    offsety = loc1a[1]-loc2b[1]
                    offsety2 = loc1b[1]-loc2a[1]
                offsetz = loc1a[2]-loc2a[2]
                offsetz2 = loc1b[2]-loc2b[2]
                if offsetz != offsetz2:
                    offsetz = loc1a[2]-loc2b[2]
                    offsetz2 = loc1b[2]-loc2a[2]
                print(f"offsetx {offsetx} {offsetx2} y {offsety} {offsety2} z {offsetz} {offsetz2}")
            elif dx1==dy2 and dy1==dx2 and dz1==dz2:
                print(f"orientation of scanners {scan1} x/y/z becomes {scan2} y/x/z")
            elif dx1==dx2 and dy1==dz2 and dz1==dy2:
                print(f"orientation of scanners {scan1} x/y/z becomes {scan2} x/z/y")
            elif dx1==dz2 and dy1==dy2 and dz1==dx2:
                print(f"orientation of scanners {scan1} x/y/z becomes {scan2} z/y/x")
            elif dx1==dy2 and dy1==dz2 and dz1==dx2:
                print(f"orientation of scanners {scan1} x/y/z becomes {scan2} y/z/x")
            elif dx1==dz2 and dy1==dx2 and dz1==dy2:
                print(f"orientation of scanners {scan1} x/y/z becomes {scan2} z/x/y")
    return matches

def part2(data):
    pass

part1(data)
part2(data)
print("Execution time:",time.time()-start)
