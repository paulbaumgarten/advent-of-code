
def maskthis2(mem, mask, target, value):
    # Any 1s in the mask, turn on in the target
    mask_or = int(mask.replace("X","0"), base=2) # Force any ones on the value... Use an OR
    target = target | mask_or
    # Turn the target into it's string binary representation
    addr_str = bin(target)[2:]
    addr_str = addr_str.rjust(36, "0") # With leading zeros
    print("Target: ",addr_str)
    print("Mask:   ",mask)
    result = 0
    for i in range(2 ** mask.count("X")):
        # Convert i into it's binary representation (without the leading `0b`)
        binary_string = bin(i)[2:]
        binary_string = binary_string.rjust(mask.count("X"), "0")
        binary_string_i = 0
        #print("BS:     ",binary_string)
        # Create a working copy of the strings so the original is not altered
        mask_instance = mask.replace("0",".").replace("1",".")
        addr_instance = addr_str
        for pos in range(len(mask)): 
            # eg: binary_string: 1001
            # eg: target before: 0000000000000
            # eg: mask_instance: .....X..XX..X
            # eg: target:        0000010000001
            if mask_instance[pos] == "X":
                addr_instance = addr_instance[:pos] + binary_string[binary_string_i] + addr_instance[pos+1:]
                binary_string_i += 1
        print("        ",addr_instance)
        mem[ int(addr_instance, base=2) ] = value
    return result

def maskthis1(mask, val):
    mask_and = int(mask.replace("X","1"), base=2) # Force any zeros on the value... Use an AND
    mask_or = int(mask.replace("X","0"), base=2) # Force any ones on the value... Use an OR
    val = (val & mask_and) | mask_or
    return val

def problem1(instr):
    mask = ""
    mem = {}
    for line in instr:
        parts = line.replace(" ","").split("=")
        if parts[0] == "mask":
            mask = parts[1]
        elif parts[0][0:3] == "mem":
            addr = parts[0][4:-1]
            mem[addr] = maskthis1(mask, int(parts[1])) 
    tot = sum(mem.values())
    print("Part 1 sum:",tot)

def problem2(instr):
    mask = ""
    mem = {}
    for line in instr:
        parts = line.replace(" ","").split("=")
        if parts[0] == "mask":
            mask = parts[1]
        elif parts[0][0:3] == "mem":
            addr = parts[0][4:-1]
            maskthis2(mem, mask, int(addr), int(parts[1])) 
    for k,v in mem.items():
        print(f"mem[{k}] = {v}")
    tot = sum(mem.values())
    print("Part 2 sum:",tot)

with open("14.txt", "r") as f:
    content = f.read().splitlines()
problem1(content)
problem2(content)
