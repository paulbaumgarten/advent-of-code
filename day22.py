# Day 22

from __future__ import annotations
import time, math

with open("day22a.txt","r") as f:
    data = f.read().splitlines()

def part1(data):
    cuboids = {}
    for instruction in data:
        inst, coords = instruction.split(" ")
        xrange,yrange,zrange = coords.split(",")
        x1,x2 = xrange[2:].split("..")
        y1,y2 = yrange[2:].split("..")
        z1,z2 = zrange[2:].split("..")
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        z1=int(z1)
        z2=int(z2)
        if x1 > x2:
            x1,x2 = x2,x1
        if y1 > y2:
            y1,y2 = y2,y1
        if z1 > z2:
            z1,z2 = z2,z1
        print(f"Processing [{inst}] for x({x1}..{x2}) y({y1}..{y2}) z({z1}..{z2})")
        if x1 >= -50 and x1 <= 50 and y1 >= -50 and y1 <= 50 and z1 >= -50 and z1 <= 50 and \
            x2 >= -50 and x2 <= 50 and y2 >= -50 and y2 <= 50 and z2 >= -50 and z2 <= 50 :
            for z in range(z1, z2+1):
                for y in range(y1, y2+1):
                    for x in range(x1, x2+1):
                        if x >= -50 and x <= 50 and y >= -50 and y <= 50 and z >= -50 and z <= 50:
                            key = (z,y,x)
                            if inst == "on":
                                cuboids[key] = 1
                            elif inst == "off":
                                if key in cuboids.keys():
                                    cuboids.pop(key)
    print(len(cuboids))

#### PART 2

class Cube:
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.inst = None
        self.parent = None
    
    def volume(self):
        return (self.x2-self.x1) * (self.y2-self.y1) * (self.z2-self.z1)
    
    def __str__(self):
        if not self.inst == None:
            return f"x({self.x1}..{self.x2}) y({self.y1}..{self.y2}) z({self.z1}..{self.z2}) volume({self.volume()}) inst({self.inst}) parent({self.parent})"
        return f"x({self.x1}..{self.x2}) y({self.y1}..{self.y2}) z({self.z1}..{self.z2}) volume({self.volume()})"
    
    def intersecting_cube(self, c:Cube):
        left = max(self.x1, c.x1)
        right = min(self.x2, c.x2)
        bottom = max(self.y1, c.y1)
        top = min(self.y2, c.y2)
        front = max(self.z1, c.z1)
        rear = min(self.z2, c.z2)
        inters = Cube(left, right, bottom, top, front, rear)
        if inters.volume() <= 0:
            return None
        else:
            return inters

    def intersecting_volume(self, c:Cube):
        if self.intersecting_cube(c) is None:
            return 0
        return self.intersecting_cube(c).volume()
    
    def remove_cube(self, c:Cube):
        # Return an array of sub-cubes that make up this cube after the intersecting portion removed
        remove = self.intersecting_cube(c)
        if remove is None:
            return [self]
        above = Cube(self.x1, self.x2, self.y1, remove.y1, self.z1, self.z2)
        below = Cube(self.x1, self.x2, remove.y2, self.y2, self.z1, self.z2)
        left = Cube(self.x1, remove.x1, remove.y1, remove.y2, self.z1, self.z2)
        right = Cube(remove.x2, self.x2, remove.y1, remove.y2, self.z1, self.z2)
        front = Cube(remove.x1, remove.x2, remove.y1, remove.y2, self.z1, remove.z1)
        back = Cube(remove.x1, remove.x2, remove.y1, remove.y2, remove.z2, self.z2)
        parts = []
        if above.volume() > 0: parts.append(above)
        if below.volume() > 0: parts.append(below)
        if left.volume() > 0: parts.append(left)
        if right.volume() > 0: parts.append(right)
        if front.volume() > 0: parts.append(front)
        if back.volume() > 0: parts.append(back)
        #print("original ",self.volume())
        #total = remove.volume()
        #for tmp in [above, below, left, right, front, back]:
        #    total += tmp.volume()
        #print("check", total)
        return parts

def part2parse(data, all=False):
    cuboids = []
    total = 0
    for instruction in data:
        inst, coords = instruction.split(" ")
        xrange,yrange,zrange = coords.split(",")
        x1,x2 = xrange[2:].split("..")
        y1,y2 = yrange[2:].split("..")
        z1,z2 = zrange[2:].split("..")
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        z1=int(z1)
        z2=int(z2)
        if x1 > x2:
            x1,x2 = x2,x1
        if y1 > y2:
            y1,y2 = y2,y1
        if z1 > z2:
            z1,z2 = z2,z1
        if all:
            c = Cube(x1,x2,y1,y2,z1,z2)
            c.inst = inst
            cuboids.append(c)
        elif x1 >= -50 and x1 <= 50 and y1 >= -50 and y1 <= 50 and z1 >= -50 and z1 <= 50 and \
            x2 >= -50 and x2 <= 50 and y2 >= -50 and y2 <= 50 and z2 >= -50 and z2 <= 50 :
            c = Cube(x1,x2,y1,y2,z1,z2)
            c.inst = inst
            cuboids.append(c)
    print(f"There are {len(cuboids)} cubes")
    return cuboids

def part2(data):
    # Test data answer 2758514936282235
    # Input data answer ?
    cuboids = part2parse(data)
    counter = 0
    i = 0
    batch_start = 0
    while i < len(cuboids):
        first = cuboids[i]
        print("Processing",i,"of",len(cuboids),":",first)
        counter += 1
        if counter == 50000:
            for z in range(len(cuboids)):
                print(z,cuboids[z])
            exit()
        j = i + 1
        j_stop = len(cuboids)
        intact = True
        while j < j_stop and intact:
            compare_to = cuboids[j]
            #print(" - comparing to",compare_to)
            if first.inst == "on" and first.intersecting_volume(compare_to) > 0:
                print(" - intersects",compare_to)
                intact = False
                batch_start = i+1
                parts = first.remove_cube(compare_to)
                for cube in parts:
                    cube.inst = "on"
                    is_in = False
                    for k in range(j+1, len(cuboids)):
                        if cube.x1 == cuboids[k].x1 and cube.x2 == cuboids[k].x2 and cube.y1 == cuboids[k].y1 and cube.y2 == cuboids[k].y2 and cube.z1 == cuboids[k].z1 and cube.z2 == cuboids[k].z2:
                            is_in = True
                            break
                    if not is_in:
                        cube.parent = i
                        cuboids.append(cube)
                        print(" - adding",cube)
                cuboids.pop(i)
                i = i-1
                #time.sleep(0.5)
            j = j + 1
        i = i + 1
    
    # Ready to total up
    total = 0
    for c in range(0, len(cuboids)):
        if cuboids[c].inst == "on":
            print("Adding cube",c,cuboids[c])
            total += cuboids[c].volume()
    print(total)

def part2again(data):
    c = part2parse(data, all=False)
    # Print the cubes
    mi = 0
    ma = 0
    for i in range(len(c)):
        mi = min(mi, c[i].x1, c[i].y1, c[i].z1)
        ma = max(ma, c[i].x2, c[i].y2, c[i].z2)
        # print("Cube",i,":",c[i])
    print("Coordinate range from ",mi, "to", ma, "range of ",(ma-mi))

    # Determine coordinate box boundaries
    x = []
    y = []
    z = []
    for i in range(len(c)):
        if c[i].x1 not in x: x.append(c[i].x1)
        if c[i].x2 not in x: x.append(c[i].x2)
        if c[i].y1 not in y: y.append(c[i].y1)
        if c[i].y2 not in y: y.append(c[i].y2)
        if c[i].z1 not in z: z.append(c[i].z1)
        if c[i].z2 not in z: z.append(c[i].z2)
        if c[i].x1 == c[i].x2: print(f"x1==x2 item {i}")
        if c[i].y1 == c[i].y2: print(f"y1==y2 item {i}")
        if c[i].z1 == c[i].z2: print(f"z1==z2 item {i}")
    x.sort()
    y.sort()
    z.sort()
    # The outermost values must also get counted, so we'll need boxes for them.
    x.append(max(x)+1)
    y.append(max(y)+1)
    z.append(max(z)+1)
    size = len(x) * len(y) * len(z)
    print(f"x: {len(x)} items, y: {len(y)} items, z: {len(z)} items = {size} boxes")
    # Allocate the memory
    boxes = [0] * size
    print(f"Allocated {size} boxes")
    # For all cuboids...
    cache = []
    for i in range(len(c)):
        print(f"Processing box {i} of {len(c)}: ",c[i])
        cube = c[i]
        my_x_boxes = []
        my_y_boxes = []
        my_z_boxes = []
        # Find the x boxes within our cuboid's range
        for j in range(0, len(x)):
            if cube.x1 <= x[j] and x[j] < cube.x2:
                my_x_boxes.append(j)
        # Find the y boxes within our cuboid's range
        for j in range(0, len(y)):
            if cube.y1 <= y[j] and y[j] < cube.y2:
                my_y_boxes.append(j)
        # Find the z boxes within our cuboid's range
        for j in range(0, len(z)):
            if cube.z1 <= z[j] and z[j] < cube.z2:
                my_z_boxes.append(j)
        # Iterate over all boxes within the cuboid's range
        for myx in my_x_boxes:
            for myy in my_y_boxes:
                for myz in my_z_boxes:
                    # Turn the box on or off as appropriate
                    box_num = myx + len(x)*myy + len(x)*len(y)*myz
                    if c[i].inst == "off":
                        print(f"Turning off box {box_num} for x({myx}) y({myy}) z({myz})")
                        boxes[box_num] = 0 # Zero volume to be counted
                    else:
                        # Determine the volume of this box
                        xrange = x[myx+1]-x[myx]
                        yrange = y[myy+1]-y[myy]
                        zrange = z[myz+1]-z[myz]
                        boxes[box_num] = xrange * yrange * zrange
                        print(f"  - x({x[myx]}..{x[myx+1]}={xrange}) y({y[myy]}..{y[myy+1]}={yrange}) z({z[myz]}..{z[myz+1]}={zrange}) volume {xrange * yrange * zrange}")
                        # Volume needs to be counted inclusive of the upper bound, so add values to the boxes representing those edges
                        # 2d planes
                        if boxes[ 1 + myx + len(x)*myy + len(x)*len(y)*myz ] == 0:
                            boxes[ 1 + myx + len(x)*myy + len(x)*len(y)*myz ] = yrange * zrange
                        if boxes[ myx + len(x)*(myy+1) + len(x)*len(y)*myz ] == 0:
                            boxes[ myx + len(x)*(myy+1) + len(x)*len(y)*myz ] = xrange * zrange
                        if boxes[ myx + len(x)*myy + len(x)*len(y)*(myz+1) ] == 0:
                            boxes[ myx + len(x)*myy + len(x)*len(y)*(myz+1) ] = xrange * yrange
                        # 1d edges
                        if boxes[ 1 + myx + len(x)*(myy+1) + len(x)*len(y)*myz ] == 0:
                            boxes[ 1 + myx + len(x)*(myy+1) + len(x)*len(y)*myz ] = zrange
                        if boxes[ myx + len(x)*(myy+1) + len(x)*len(y)*(myz+1) ] == 0:
                            boxes[ myx + len(x)*(myy+1) + len(x)*len(y)*(myz+1) ] = xrange
                        if boxes[ 1 + myx + len(x)*myy + len(x)*len(y)*(myz+1) ] == 0:
                            boxes[ 1 + myx + len(x)*myy + len(x)*len(y)*(myz+1) ] = yrange
                        # 1 pixel corners
                        # TO-DO

    # Sum all the boxes to find our answer
    print("Summing...")
    a = sum(boxes)
    print(a, a-590784)
    print(sum(cache))

### PART 1
# Test data answer 590784
# Input data answer 652209

# part1(data)
part2again(data)
