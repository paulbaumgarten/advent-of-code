
FILE = "./2023/2023-08.txt"

TEST1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

TEST2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    steps = data[0]
    nodes = {}
    aaa = 0
    zzz = 0
    for i in range(2, len(data)):
        loc = data[i][0:3]
        left = data[i][7:10]
        right = data[i][12:15]
        nodes[loc] = (left, right)
    print(nodes,"\n\n")
    print("AAA:",nodes["AAA"], "ZZZ:",nodes["ZZZ"])
    print("JXN:", nodes["JXN"])
    total = 0
    step = 0
    reset = 0
    now = 'AAA'
    while now != 'ZZZ':
        print(total,now,nodes[now],steps[step])
        if steps[step] == 'L':
            now = nodes[now][0]
        else:
            now = nodes[now][1]
        total += 1
        step += 1
        if step >= len(steps): 
            step = 0
            reset += 1
            print(f"Resetting step: occurance {reset}")
    print(total)

def part2():
    def now_set_all_zzz(nows):
        for k in nows:
            if k[2] != 'Z':
                return False
        return True

    with open(FILE, "r") as f:
        data = f.read().splitlines()
    steps = data[0]
    nodes = {}
    for i in range(2, len(data)):
        loc = data[i][0:3]
        left = data[i][7:10]
        right = data[i][12:15]
        nodes[loc] = (left, right)
    print(nodes,"\n\n")
    total = 0
    now_set = []
    for k,v in nodes.items():
        if k[2] == 'A':
            now_set.append(k)
    print("now_set",now_set)
    solutions = []
    for i in range(0, len(now_set)):
        step = 0
        reset = 0
        total_this_ghost = 0
        while now_set[i][2] != 'Z':
            #print(i,total_this_ghost,now_set[i],nodes[now_set[i]],steps[step])
            if steps[step] == 'L':
                now_set[i] = nodes[now_set[i]][0]
            else:
                now_set[i] = nodes[now_set[i]][1]
            step += 1
            total_this_ghost += 1
            if step >= len(steps): 
                step = 0
                reset += 1
                #print(f"Resetting step: occurance {reset}")
        print(now_set[i], step, total_this_ghost)
        solutions.append(total_this_ghost)
    n = solutions[0]
    c = 0
    while True:
        solved = True
        for soln in solutions:
            if n % soln != 0:
                solved = False
                break
        if solved: break
        n += solutions[0]
        c += 1
        if c % 1000000==0:
            print(c,n)
    print(n)

#part1()
part2()

# 10818234074807
