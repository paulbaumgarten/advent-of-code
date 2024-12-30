import math, random, numpy, os, re, copy, time

EX = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0""".splitlines()

EX2 = """Register A: 117440
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

class Program:
    def __init__(self, prog, a, b, c, debug=True):
        self.prog = prog
        self.a = a
        self.b = b
        self.c = c
        self.instruction_pointer = 0
        self.debug=debug
        if self.debug: print(f"Program: {prog}, A: {a}, B: {b}, C: {c}")
        self.output = []
    
    def combo_operand(self, val):
        if val <= 3:
            return val
        if val == 4:
            return self.a
        if val == 5:
            return self.b
        if val == 6:
            return self.c
        print("ERROR - Should not be here.")
        return None
    
    def instruction(self, code, operand):
        if code == 0: # adv - division
            numerator = self.a
            denominator = 2**self.combo_operand(operand)
            if self.debug: print(f"adv {numerator} {denominator}")
            self.a = numerator // denominator
            self.instruction_pointer += 2
            return self.a
        if code == 1: # bxl - bitwise xor
            if self.debug: print(f"bxl {self.b} {operand}")
            self.b = self.b ^ operand
            self.instruction_pointer += 2
            return self.b
        if code == 2: # bst - mod 8
            if self.debug: print(f"bst {self.b} {operand}")
            self.b = self.combo_operand(operand) % 8
            self.instruction_pointer += 2
            return self.b
        if code == 3: # jnz = jump if a not 0
            if self.debug: print(f"jnz {self.a} {operand}")
            if self.a == 0:
                self.instruction_pointer += 2
                return False
            else:
                self.instruction_pointer = operand
                return True
        if code == 4: # bxc - bitwise xor
            if self.debug: print(f"bxc {self.b} {self.c}")
            self.b = self.b ^ self.c
            self.instruction_pointer += 2
            return self.b
        if code == 5: # out
            if self.debug: print(f"out {operand}")
            output = self.combo_operand(operand) % 8
            self.output.append(output)
            if self.debug: print(f"output = {output}")
            self.instruction_pointer += 2
            return output
        if code == 6: # bdv
            numerator = self.a
            denominator = 2**self.combo_operand(operand)
            if self.debug: print(f"bdv {numerator} {denominator}")
            self.b = numerator // denominator
            self.instruction_pointer += 2
            return self.b
        if code == 7: # cdv
            numerator = self.a
            denominator = 2**self.combo_operand(operand)
            if self.debug: print(f"cdv {numerator} {denominator}")
            self.c = numerator // denominator
            self.instruction_pointer += 2
            return self.c
    
    def execute(self):
        while self.instruction_pointer < len(self.prog):
            self.instruction(self.prog[self.instruction_pointer], self.prog[self.instruction_pointer+1])

    def get_outputs(self):
        output = [str(n) for n in self.output]
        return ",".join(output)


def part1(raw):
    data = EX[:]
    data = raw[:]
    reg_a = int(data[0][12:])
    reg_b = int(data[1][12:])
    reg_c = int(data[2][12:])
    prog = [int(n) for n in data[4][9:].split(",")]
    p = Program(prog, reg_a, reg_b, reg_c)
    p.execute()
    print(p.get_outputs())
    return p.get_outputs()

def part2(raw):
    data = EX2[:]
    data = raw[:]
    reg_a = int(data[0][12:])
    reg_b = int(data[1][12:])
    reg_c = int(data[2][12:])
    prog_str = data[4][9:]
    prog = [int(n) for n in data[4][9:].split(",")]
    # a = 128600000
    a = 109019476330651
    p = Program(prog, a, reg_b, reg_c, False)
    p.execute()
    print(p.get_outputs())
    a = 109019473641472
    while True:
        p = Program(prog, a, reg_b, reg_c, False)
        p.execute()
        if a % 100000 == 0:
            print("A:",a,"=>",p.get_outputs())
        if p.get_outputs() == "2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0":
            print(f"The required value for A is {a} => {p.get_outputs()}")
            return a
        a += 1

def run(a):
    # 2,4 b = a % 8
    # 1,5 b = b ^ 5
    # 7,5 c = a // 2**b
    # 0,3 a = a // 2**3 
    # 4,0 b = b ^ c
    # 1,6 b = b ^ 6
    # 5,5 output b % 8
    # 3,0 return to start if a!=0
    b = a % 8
    b = b ^ 5
    c = a // 2**b
    a = a // 2**3 
    b = b ^ c
    b = b ^ 6
    print(b % 8)
    return a != 0
"""
if __name__=="__main__":
    for i in range(0,8*8):
        #print("i",i, "a!=0?",run(i))
        p = Program([2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0], i, 0, 0, False)
        p.execute()
        print(p.get_outputs())

2,4,1,5
2203
100 010 011 011
100010011011

2,4,1,5,7,5,0,3,
4,0,1,6,5,5,3,0

7,5,0,3
2649
101 001 011 001 
101001011001

4,0,1,6

5,5,3,0
1538

4,0,1,6,5,5,3,0
6498067
011000110010011100010011
011 000 110 010 011 100 010 011

bin(2649)+bin(2203)
int("101001011001100010011011",base=2)
10852507

011000110010011100010011 101001011001100010011011
011000110010011100010011000000000000000000000000
011000110010011100010011101001011001100010011011
109019484493979

The required value for A is 12093850 => 2,4,1,5,7,5,0,3
Part 2 result: 12093850

109019473641472

"""

"""
run 0=> 3
    1   2
    2   1
    3   0
    4   5
    5   3
    6   5
    7   5


2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0

1,
"""

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")
"""

# 128 600 000

Register A: 46187030
Register B: 0
Register C: 0

Program: 2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0

2,4 b = a % 8
1,5 b = b ^ 5
7,5 c = a // 2**b
0,3 a = a // 2**3 
4,0 b = b ^ c
1,6 b = b ^ 6
5,5 output b % 8
3,0 return to start if a!=0

"""

