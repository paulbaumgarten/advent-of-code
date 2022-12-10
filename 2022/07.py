from pprint import pprint

with open("./2022/day7.txt", "r") as f:
    data = f.read().splitlines()

tree = {}
subtrees = []

def ls(current, data, instr):
    instr = instr+1
    parts = data[instr].split(" ")
    while parts[0] != "$" and instr < len(data):
        print("processing: ",data[instr])
        if parts[0] == "dir":
            dirname = parts[1]
            current[dirname] = {}
        else:
            filesize = int(parts[0])
            filename = parts[1]
            current[filename] = filesize
        instr += 1
        if instr == len(data): break
        parts = data[instr].split(" ")
    print("exiting")
    return None

sizes = []
names = []

def get_folder_sizes_part1(name, subtree):
    print(f"get_folder_sizes({name})")
    total = 0
    for k,v in subtree.items():
        if type(v) == dict: # means k is a folder
            total = total + get_folder_sizes_part1(k, subtree[k])
        else: # k is a file
            total = total + subtree[k]
    if total <= 100000:
        sizes.append(total)
    return total

def get_folder_sizes_part2(name, subtree):
    print(f"get_folder_sizes({name})")
    total = 0
    for k,v in subtree.items():
        if type(v) == dict: # means k is a folder
            total = total + get_folder_sizes_part2(k, subtree[k])
        else: # k is a file
            total = total + subtree[k]
    sizes.append(total)
    names.append(name)
    return total

def part1(data):
    # Build the tree
    current = tree
    for instr in range(0, len(data)):
        parts = data[instr].split(" ")
        if parts[0] == "$" and parts[1] == "cd":
            if parts[2] == "/": # cd /
                current = tree
            elif parts[2] == "..": # cd ..
                print("going back one:",subtrees)
                current = subtrees.pop()
            else: # cd into named folder
                newfolder = parts[2]
                current[newfolder] = {} # new subtree for this folder
                subtrees.append(current)
                current = current[newfolder]
        if parts[0] == "$" and parts[1] == "ls":
            ls(current, data, instr)
    pprint(tree)
    # Find folder sizes
    total = get_folder_sizes_part1("/", tree)
    print("grand total",total)
    print("part a answer",sum(sizes))

def part2(data):
    # Build the tree
    current = tree
    for instr in range(0, len(data)):
        parts = data[instr].split(" ")
        if parts[0] == "$" and parts[1] == "cd":
            if parts[2] == "/": # cd /
                current = tree
            elif parts[2] == "..": # cd ..
                print("going back one:",subtrees)
                current = subtrees.pop()
            else: # cd into named folder
                newfolder = parts[2]
                current[newfolder] = {} # new subtree for this folder
                subtrees.append(current)
                current = current[newfolder]
        if parts[0] == "$" and parts[1] == "ls":
            ls(current, data, instr)
    pprint(tree)
    # Find folder sizes
    total = get_folder_sizes_part2("/", tree)
    print("grand total",total)
    space_available = 70000000 - total
    space_needed = 30000000 - space_available
    print("space needed",space_needed)
    smallest = -1
    for i in range(len(sizes)):
        print(sizes[i], names[i])
        if sizes[i] >= space_needed and (smallest==-1 or sizes[i]<sizes[smallest]):
            smallest = i
    print("part b answer: smallest found at position",smallest, "of size",sizes[smallest], "named",names[smallest])

part2(data)

