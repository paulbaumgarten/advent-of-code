import math

def problem1(directions):
    facing = 90
    north = 0
    east = 0
    for d in directions:
        print(f"From {north}N {east}E facing {facing}: Doing {d['op']} val {d['value']}")
        if d['op'] == "N":
            north += d['value']
        elif d['op'] == "S":
            north -= d['value']
        elif d['op'] == "E":
            east += d['value']
        elif d['op'] == "W":
            east -= d['value']
        elif d['op'] == "R": # Rotate clockwise
            facing = (facing + d['value']) % 360
        elif d['op'] == "L": # Rotate anticlockwise
            facing = (facing - d['value']) % 360
        elif d['op'] == "F": # Forward
            if facing == 0:
                north += d['value']
            elif facing == 90:
                east += d['value']
            elif facing == 180:
                north -= d['value']
            elif facing == 270:
                east -= d['value']
            else:
                angle = math.radians(facing)
                hyp = d['value']
                opp = hyp / math.sin(angle)
                adj = hyp / math.cos(angle)
                print(f"Forward {hyp} at angle {facing} is delta north {adj}, east {opp}")
                north += adj
                east += opp
    print(f"Final location is delta north {north}, east {east}")
    print(f"Manhattan distance: {abs(north) + abs(east)}")


def problem2(directions):
    waypoint = [1, 10]
    travelled = [0,0]
    for d in directions:
        #print(f"From {north}N {east}E facing {facing}: Doing {d['op']} val {d['value']}")
        if d['op'] == "N":
            waypoint[0] += d['value']
        elif d['op'] == "S":
            waypoint[0] -= d['value']
        elif d['op'] == "E":
            waypoint[1] += d['value']
        elif d['op'] == "W":
            waypoint[1] -= d['value']
        elif d['op'] == "R": # Rotate clockwise
            if d['value'] == 90:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            elif d['value'] == 180:
                waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
            elif d['value'] == 270:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif d['op'] == "L": # Rotate anticlockwise
            d['value'] = 360 - d['value']
            if d['value'] == 90:
                waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
            elif d['value'] == 180:
                waypoint[0], waypoint[1] = -waypoint[0], -waypoint[1]
            elif d['value'] == 270:
                waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
        elif d['op'] == "F": # Forward
            travelled[0] += waypoint[0] * d['value']
            travelled[1] += waypoint[1] * d['value']
    print(f"Final location is delta {travelled}")
    print(f"Manhattan distance: {abs(travelled[0]) + abs(travelled[1])}")


with open("11.txt", "r") as f:
    content = f.read().splitlines()

directions = []
for line in content:
    instr = { "op": line[0], "value": int(line[1:])}
    directions.append(instr)

#problem1(directions)
problem2(directions)
