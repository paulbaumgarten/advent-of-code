# Day 24 - Op-code ALU


def alu(code, inputs):
    """
    inp a - Read input and store in a
    add a b - a = a+b
    mul a b - a = a*b
    div a b - a = int(a/b)
    mod a b - a = a%b
    eql a b - a = a==b ? 1 : 0
    """

    # Initialise registers
    reg = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    # Track inputs read from the buffer
    inputs_read = 0
    # Process the op-code
    for line in code:
        op, op_vars = line.split(" ", 1)
        if op == "inp":
            reg[op_vars] = int(inputs[inputs_read])
            inputs_read+=1
        else:
            v1, v2 = op_vars.split(" ")
            if op == "add":
                if v2 in ['w','x','y','z']:
                    reg[v1] = reg[v1] + reg[v2]
                else:
                    reg[v1] = reg[v1] + int(v2)
            elif op == "mul":
                if v2 in ['w','x','y','z']:
                    reg[v1] = reg[v1] * reg[v2]
                else:
                    reg[v1] = reg[v1] * int(v2)
            elif op == "div":
                if v2 in ['w','x','y','z']:
                    reg[v1] = reg[v1] // reg[v2]
                else:
                    reg[v1] = reg[v1] // int(v2)
            elif op == "mod":
                if v2 in ['w','x','y','z']:
                    reg[v1] = reg[v1] % reg[v2]
                else:
                    reg[v1] = reg[v1] % int(v2)
            elif op == "eql":
                if v2 in ['w','x','y','z']:
                    reg[v1] = 1 if reg[v1] == reg[v2] else 0
                else:
                    reg[v1] = 1 if reg[v1] == int(v2) else 0
            else:
                print("Error, unrecognised opcode")
    #print(f"w x y z\n{reg['w']} {reg['x']} {reg['y']} {reg['z']}")
    return (reg['w'], reg['x'], reg['y'], reg['z'])

with open("day24.txt", "r") as f:
    data = f.read().splitlines()

# Part 1
valid = False
serial = "99999999999999"
counter = 0
while not valid:
    if counter % 100000 == 0:
        print(f"Trying serial {serial}")
    counter += 1
    w,x,y,z = alu(data, serial)
    valid = True if z == 0 else False
    if valid: break
    serial = str(int(serial)-1)
    while "0" in serial:
        serial = str(int(serial)-1)
print(serial)