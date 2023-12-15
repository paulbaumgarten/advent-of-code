
FILE = "./2023/2023-15.txt"

TEST = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".splitlines()

def hash(inp):
    res = 0
    for i in range(0, len(inp)):
        res += ord(inp[i])
        res *= 17
        res %= 256
    return res

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    data = data[0].split(",")
    total = 0
    for datum in data:
        total += hash(datum)
    print(total)

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    data = data[0].split(",")
    boxes = [0 for _ in range(256)]
    lenses = [[] for _ in range(256)]

    # Lenses shuffle
    for i in range(0, len(data)):
        lens = data[i]
        if "-" in lens: # Dash
            label = lens.replace("-","")
            b = hash(label)
            n = 0
            while n < len(lenses[b]):
                if lenses[b][n][0] == label:
                    lenses[b].pop(n)
                else:
                    n+=1
        elif "=" in lens: # Equals
            label, focal = lens.split("=")
            focal = int(focal)
            b = hash(label)
            n = 0
            updated = False
            while n < len(lenses[b]):
                if lenses[b][n][0] == label:
                    lenses[b][n] = (label,focal)
                    updated = True
                    break
                else:
                    n+=1
            if not updated:
                lenses[b].append((label,focal))
        # Print sanity check
        print(f"After {lens}")
        for b in range(0,len(lenses)):
            print(f"Box {b}: {lenses[b]}")
    # Focus power
    power = 0
    for b in range(0, len(boxes)):
        for slot in range(0, len(lenses[b])):
            power += (b+1) * (slot+1) * lenses[b][slot][1]
    print(power)

part1()
part2()

