import math, random, numpy, os, re, copy, time

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().split("\n\n")
    return data

### Today's problem

"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

    x => a*94 + b*22 = 8400
    y => a*34 + b*67 = 5400

"""

DEMO = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".split("\n\n")

def process(xa,ya,xb,yb,x_prize,y_prize):
    # xa * a_press + xb * b_press = x_prize
    # ya * a_press + yb * b_press = y_prize

    # a_press = (x_prize - xb * b_press) / xa
    # b_press = (y_prize - ya * a_press) / yb

    print(f"""Button A: X+{xa}, Y+{ya}
Button B: X+{xb}, Y+{yb}
Prize: X={x_prize}, Y={y_prize}\n""")

    a_press = (x_prize*yb - xb*y_prize) / (xa*yb - ya*xb)
    b_press = (y_prize - ya * a_press) / yb

    if a_press % 1.0 == 0.0 and b_press % 1.0 == 0.0:
        print(f"a {a_press} b {b_press}\n")
        return 3*a_press + b_press
    else:
        print("No solution\n")
        return 0

def part1(raw):
    data = DEMO[:]
    data = raw[:]
    tokens = 0
    for i,equation in enumerate(data):
        # print(equation)
        equation = equation.split("\n")
        button_a = equation[0][10:].split(", ")
        button_b = equation[1][10:].split(", ")
        prize = equation[2][7:].split(", ")
        xa = int(button_a[0][2:])
        ya = int(button_a[1][2:])
        xb = int(button_b[0][2:])
        yb = int(button_b[1][2:])
        xp = int(prize[0][2:])
        yp = int(prize[1][2:])
        tokens += process(xa,ya,xb,yb,xp,yp)
    return tokens

def part2(raw):
    data = DEMO[:]
    data = raw[:]
    tokens = 0
    correction = 10000000000000
    for i,equation in enumerate(data):
        # print(equation)
        equation = equation.split("\n")
        button_a = equation[0][10:].split(", ")
        button_b = equation[1][10:].split(", ")
        prize = equation[2][7:].split(", ")
        xa = int(button_a[0][2:])
        ya = int(button_a[1][2:])
        xb = int(button_b[0][2:])
        yb = int(button_b[1][2:])
        xp = int(prize[0][2:])+correction
        yp = int(prize[1][2:])+correction
        tokens += process(xa,ya,xb,yb,xp,yp)
    return tokens

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


