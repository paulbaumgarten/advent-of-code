# Day 17

import math, time

data = [
    "target area: x=20..30, y=-10..-5",
    "target area: x=175..227, y=-134..-79"
]

def parse(datum):
    if datum[0:13] != "target area: ":
        print("Parsing error 1")
        return None
    x_part, y_part = datum[13:].split(", ")
    if x_part[0:2] != "x=" or y_part[0:2] != "y=":
        print("Parsing error 2")
        return None
    x = x_part[2:].split("..")
    y = y_part[2:].split("..")
    return (int(x[0]), int(x[1]), int(y[0]), int(y[1]))

def find_x_range(datum):
    x_range = []
    for vx in range(228):
        t = -1
        found = False
        while t<100000 and not found:
            t = t+1
            found = False
            x = -0.5*(t**2) + (vx+0.5)*t
            if x > datum[1]:
                # print(f"vx {vx} vy {vy} t{t} point {x},{y} datum {datum} - abort")
                break
            if x >= datum[0] and x<= datum[1]:
                print(f"vx {vx}, t {t} = {x}")
                x_range.append({"vx":vx, "t":t, "x":x})
                found = True
    return x_range

def part1(datum):
    # y = -0.5*(t**2) + (v[1]+0.5)*t
    dataset = find_x_range(datum)
    for i in range(0, len(dataset)):
        t = dataset[i]["t"]
        for vy in range(-1000, 10000):
            y = -0.5*(t**2) + (vy+0.5)*t
            if y >= datum[2] and y <= datum[3]:
                dataset[i]["y"] = y
                dataset[i]["vy"] = vy
    print()
    for i in range(0, len(dataset)):
        if "vy" in dataset[i].keys():
            print(dataset[i])
    maxy = -math.inf
    for i in range(0, len(dataset)):
        if "vy" in dataset[i].keys():
            vx = dataset[i]["vx"]
            vy = dataset[i]["vy"]
            print(f"vx {vx} vy {vy}")
            for t in range(0, dataset[i]["t"]+1):
                y = -0.5*(t**2) + (vy+0.5)*t
                if y > maxy:
                    print(f"new maxy t={t} y={y}")
                    maxy = y
    print(maxy)
    return dataset

# part1(parse(data[1])) # 1176 too low, #1225 too low
# ...227
# vx=19 works ... 1176 with y=-3 to 48
# velocity x 20 y 49 step 100 raeached location x 210 y -101 IN TARGET. MAXY was 1225
# velocity x 19 y 49 step 100 raeached location x 190 y -101 IN TARGET. MAXY was 1225

# You know what...
# I give up... too tired... instead of doing it the "proper" math-y way, I'm just going to brute force this!

datum = [175, 227, -134, -79]
supermaxy = -999999999
count = 0
for original_vx in range(0,1500):
    print(original_vx, count)
    for original_vy in range(-140,250):
        x=0
        y=0
        vx = original_vx
        vy = original_vy
        maxy = -999999999
        for i in range(0,10000):
            x = x + vx
            y = y + vy
            vx = vx - 1
            if vx < 0:
                vx = 0
            if y > maxy:
                maxy = y
            vy = vy - 1
            if x >= datum[0] and x <= datum[1] and y >= datum[2] and y <= datum[3]:
                count = count + 1
                if maxy > 1000:
                    print(f"velocity x {original_vx} y {original_vy} step {i} raeached location x {x} y {y} IN TARGET. MAXY was {maxy}")
                if maxy > supermaxy:
                    supermaxy = maxy
                break
            #if x >= datum[1]:
            #    print(f"x {x}")
            #    break
print("supermaxy",supermaxy) # 8911
print("count",count) # 4748
print("end")
