
FILE = "./2023/2023-09.txt"

TEST = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    total = 0
    for i in range(0, len(data)):
    #for i in range(158, 159):
        sequence = [int(n) for n in data[i].split(" ")]
        print(f"Sequence {i} = {sequence}")
        layers = [sequence]
        curr_layer = 0
        # Work down
        diff = -1
        while diff != 0:
            new_layer = []
            diff = 0
            for j in range(0, len(layers[curr_layer])-1):
                new_layer.append(layers[curr_layer][j+1] - layers[curr_layer][j])
                diff += abs(layers[curr_layer][j+1] - layers[curr_layer][j])
            layers.append(new_layer)
            curr_layer += 1
        #print(layers)
        # Work up
        for n in range(len(layers)-2,-1,-1):
            diff = layers[n+1][len(layers[n+1])-1]
            last_val = layers[n][len(layers[n])-1]
            layers[n].append(last_val+diff)
        for z in range(0,len(layers)):
            print(layers[z])
        # Add to total
        print("Adding",layers[0][len(layers[0])-1])
        total += (layers[0][len(layers[0])-1])
    print(total)
    # 1688874534
    # 1696382054
    # 1702218515

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    total = 0
    for i in range(0, len(data)):
    #for i in range(158, 159):
        sequence = [int(n) for n in data[i].split(" ")]
        print(f"Sequence {i} = {sequence}")
        layers = [sequence]
        curr_layer = 0
        # Work down
        diff = -1
        while diff != 0:
            new_layer = []
            diff = 0
            for j in range(0, len(layers[curr_layer])-1):
                new_layer.append(layers[curr_layer][j+1] - layers[curr_layer][j])
                diff += abs(layers[curr_layer][j+1] - layers[curr_layer][j])
            layers.append(new_layer)
            curr_layer += 1
        #print(layers)
        # Work up
        for n in range(len(layers)-2,-1,-1):
            diff = layers[n+1][0]
            first_val = layers[n][0]
            layers[n].insert(0, first_val-diff)
        for z in range(0,len(layers)):
            print(layers[z])
        # Add to total
        print("Adding",layers[0][0])
        total += (layers[0][0])
    print(total)
    
#part1()
part2()

