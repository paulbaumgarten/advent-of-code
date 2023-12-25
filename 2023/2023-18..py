from PIL import Image, ImageDraw


FILE = "./2023/2023-18.txt"

TEST = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".splitlines()

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    # Obtain max dimensions and offsets
    y,x = 0,0
    miny, minx, maxy, maxx = 0,0,0,0
    for i in range(0, len(data)):
        dir, qty, color = data[i].split(" ")
        qty = int(qty)
        if dir == "U":
            y=y-qty
            if y < miny: miny=y
        if dir == "D":
            y=y+qty
            if y > maxy: maxy=y
        if dir == "L":
            x=x-qty
            if x < minx: minx=x
        if dir == "R":
            x=x+qty
            if x > maxx: maxx=x
    w = maxx-minx+1
    h = maxy-miny+1
    # Now put it into a grid
    print(f"y from {miny} to {maxy}; x from {minx} to {maxx}")
#    grid = [["." for x in range(w)] for y in range(h)]
    grid = [["." for x in range(w)] for y in range(h)]
    offsety=-miny
    offsetx=-minx
    y,x=0,0
    grid[offsety+y][offsetx+x] = "#"
    for i in range(0, len(data)):
        dir, qty, color = data[i].split(" ")
        qty = int(qty)
        grid[offsety+y][offsetx+x] = "#"
        print(f"From y {y}, x {x} go {dir} for {qty} (siee is {len(grid)} x {len(grid[0])})")
        if dir == "U":
            for n in range(y-qty+1,y+1):
                #print("  ",offsety+n, offsetx+x)
                grid[offsety+n][offsetx+x] = "#"
            y-=qty
        if dir == "D":
            for n in range(y+1,y+qty+1):
                grid[offsety+n][offsetx+x] = "#"
            y+=qty
        if dir == "L":
            for n in range(x-qty+1,x+1):
                grid[offsety+y][offsetx+n] = "#"
            x-=qty
        if dir == "R":
            for n in range(x+1,x+qty+1):
                grid[offsety+y][offsetx+n] = "#"
            x+=qty
        #for n in range(0, h):
        #    print("".join(grid[n]))
    #print()
    # Flood fill
    if True:
        q = [(offsety+1,offsetx+1)]
        while len(q) > 0:
            y,x = q.pop()
            if grid[y-1][x] == '.': q.append((y-1,x))
            if grid[y+1][x] == '.': q.append((y+1,x))
            if grid[y][x-1] == '.': q.append((y,x-1))
            if grid[y][x+1] == '.': q.append((y,x+1))
            grid[y][x] = "#"
    # Draw
    for y in range(0, h):
        print("".join(grid[y]))
    # Count
    total = 0
    for y in range(h):
        total += ("".join(grid[y])).count("#")
    print(total)

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    img = Image.new("RGBA", (1000,1000))

    DRAW = True
    # Obtain max dimensions and offsets
    directions = []
    directions.append((0,0,0,0))
    y,x = 0,0
    miny, minx, maxy, maxx = 0,0,0,0
    for i in range(0, len(data)):
        dir, qty, color = data[i].split(" ")
        parts = color.split("#")[1]
        qty = int(parts[0:5],base=16)
        match parts[5]:
            case "0": dir="R"
            case "1": dir="D"
            case "2": dir="L"
            case "3": dir="U"
        if dir == "U":
            y=y-qty
            if y < miny: miny=y
        if dir == "D":
            y=y+qty
            if y > maxy: maxy=y
        if dir == "L":
            x=x-qty
            if x < minx: minx=x
        if dir == "R":
            x=x+qty
            if x > maxx: maxx=x
        directions.append((y,x,dir,qty))
    w = maxx-minx+1
    h = maxy-miny+1
    print(directions)
    for d in directions:
        print(d)
    # Now put it into a grid
    print(f"y from {miny} to {maxy}; x from {minx} to {maxx}")
    # Calculate area of the polygon
    total = 0
    for i in range(0, len(directions)-1):
        y1,x1,_,_ = directions[i]
        y2,x2,_,_ = directions[i+1]
        y1,x1,y2,x2=y1+1,x1+1,y2+1,x2+1
        total += x1*y2 - x2*y1
        print(f"Adding {i} {x1*y2 - x2*y1}    from yx {y1},{x1} to yx {y2},{x2}")
        if DRAW:
            draw = ImageDraw.Draw(img)
            draw.line((x1//2000,y1//2000,x2//2000,y2//2000), fill=(255,0,0), width=3)

    y1,x1,_,_ = directions[len(directions)-1]
    y2,x2,_,_ = directions[0]
    y1,x1,y2,x2=y1+1,x1+1,y2+1,x2+1
    total += x1*y2 - x2*y1
    if DRAW:
        draw = ImageDraw.Draw(img)
        draw.line((x1//2000,y1//2000,x2//2000,y2//2000), fill=(0,0,255), width=3)
    print(f"Adding {i} {x1*y2 - x2*y1}    from yx {y1},{x1} to yx {y2},{x2}")
    total = 0.5 * abs(total)
    print(total)
    edges = 0
    for z in range(0, len(directions)):
        edges += directions[z][3]
    print(total+edges/2+1)
    img.show()
    
#part1()
part2()

# y from -9623536 to 347499; x from -1727113 to 10433666
# 9971035 x 12160779
# 121255553036265 .... 10^14  10^12

# https://www.linkedin.com/advice/1/how-do-you-calculate-area-perimeter-irregular-polygon#:~:text=To%20calculate%20the%20area%20of,is%20the%20number%20of%20vertices.
# A = 0.5 * |(x1*y2 - x2*y1) + (x2*y3 - x3*y2) + ... + (xn*y1 - x1*yn)|

# correct  952408144115
# getting  952404941483.0
# under by      3202632

# correct  952408144115
# getting  952411346745.0
# over by       3202630

#          952408144114.0

