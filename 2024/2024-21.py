import math, random, numpy, os, re, copy, time

EX = """029A
980A
179A
456A
379A""".splitlines()

REAL = """973A
836A
780A
985A
413A""".splitlines()

### Today's problem

class NumericKeypad:
    def __init__(self):
        self.pos = "A"
        self.y = 3
        self.x = 2
        self.grid = [["7","8","9"],
                     ["4","5","6"],
                     ["1","2","3"],
                     [False,"0","A"]]
        self.sequence = []
    
    def find(self, val):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == val:
                    return [y,x]
    
    def move_to(self, val):
        action = self.pos+val
        if action in ["74","85","96","41","52","63","20","3A"]: self.sequence.append( ["vA"] )
        if action in ["71","82","93","50","6A"]: self.sequence.append( ["vvA"] )
        if action in ["80","9A"]: self.sequence.append( ["vvvA"] )
        if action in ["78","45","12","89","56","23","0A"]: self.sequence.append( [">A"] )
        if action in ["79","46","13"]: self.sequence.append( [">>A"] )

        if action in ["47","58","69","14","25","36","02","A3"]: self.sequence.append( ["^A"] )
        if action in ["17","28","39","05","A6"]: self.sequence.append( ["^^A"] )
        if action in ["08","A9"]: self.sequence.append( ["^^^A"] )
        if action in ["87","54","21","98","65","32","A0"]: self.sequence.append( ["<A"] )
        if action in ["97","64","31"]: self.sequence.append( ["<<A"] )
        # 50
        if action in ["75","86","42","53","2A"]: self.sequence.append( [">vA","v>A"] )
        if action in ["10"]: self.sequence.append( [">vA"] )
        if action in ["76","43"]: self.sequence.appeal( [">>vA","v>>A"])
        if action in ["1A"]: self.sequence.append( [">>vA",">v>A"] )

        if action in ["57","68","24","35","A2"]: self.sequence.append( ["<^A","^<A"] )
        if action in ["01"]: self.sequence.append( ["^<A"] )
        if action in ["67","34"]: self.sequence.appeal( ["<<^A","^<<A"])
        if action in ["A1"]: self.sequence.append( ["^<<A","<^<A"] )
        # 68
        if action in ["72","83","5A"]: self.sequence.append( ["vv>A",">vvA"] )
        if action in ["27","38","A5"]: self.sequence.append( ["<^^A","^^<A"] )
        if action in ["40"]: self.sequence.append( ["v>vA",">vvA"] )
        if action in ["04"]: self.sequence.append( ["^<^A","^^<A"] )
        
        if action in ["70"]: self.sequence.append( ["vv>vA",">vvvA"] )
        if action in ["07"]: self.sequence.append( ["^^^<A","^<^^A"] )
        if action in ["8A"]: self.sequence.append( [">vvvA","vvv>A"] )
        if action in ["A8"]: self.sequence.append( ["<^^^A","^^^<A"] )

        if action in ["73"]: self.sequence.append(["vv>>A",">>vvA"])
        if action in ["37"]: self.sequence.append(["^^<<A","<<^^A"])
        # 82
        if action in ["00","AA","11","22","33","44","55","66","77","88","99"]: self.sequence.append(["A"])
        # 92
        if action in ["84","95","51","62","30"]: self.sequence.append(["v<A","<vA"])
        if action in ["48","59","15","26","03"]: self.sequence.append(["^>A",">^A"])
        if action in ["94","61"]: self.sequence.append(["v<<A","vv<A"])
        if action in ["49","16"]: self.sequence.append(["^>>A",">>^A"])
        if action in ["81","92","60"]: self.sequence.append(["vv<A","<vvA"])
        if action in ["18","29","06"]: self.sequence.append(["^^>A",">^^A"])
        if action in ["91"]: self.sequence.append(["vv<<A","<<vvA"])
        if action in ["19"]: self.sequence.append(["^^>>A",">>^^A"])
        if action in ["90"]: self.sequence.append(["<vvvA","vvv<A"])
        if action in ["09"]: self.sequence.append(["^^^>A",">^^^A"])
        if action in ["A4"]: self.sequence.append(["^^<<A","<^^<A","^<^<A","<^<^A"])
        if action in ["4A"]: self.sequence.append(["v>>vA",">>vvA","v>v>A"])
        if action in ["A8"]: self.sequence.append(["<^^^A","^^^<A"])
        if action in ["8A"]: self.sequence.append([">vvvA","vvv>A"])
        # 116
        self.pos = val
    
    def get_sequence(self):
        return "".join(self.sequence)


# ^A^^<<A>>AvvvA

#  -  ^  A
#  <  v  >

# <A >A <A A v<A A >>^A vA A ^A v<A A A >^A
# <A >A <A A <vA A ^>>A vA A ^A <vA A A ^>A - my generated

# <<vA^>>AvA^A<<vA^>>AA<<vA>A^>AA<A>vAA^A<vA^>AA<A>A<<vA>A^>AAA<A>vA^A

# v<A<A>>^A
# v<<A>A>^A

class DirectionalKeypad:
    def __init__(self):
        self.pos = "A"
        self.y = 0
        self.x = 2
        self.sequence = []
        self.grid = [[False,"^","A"],
                     ["<","v",">"]]

    def find(self, val):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == val:
                    return [y,x]
    
    def move_to(self, val):
        move = []
        if self.pos == "A":
            if val == "A": move.append( ["A"] )
            if val == "<": move.append( ["v<<A","<v<A"] )
            if val == "^": move.append( ["<A"] )
            if val == "v": move.append( ["v<A","<vA"] )
            if val == ">": move.append( ["vA"] )
        if self.pos == "<":
            if val == "A": move.append( [">>^A",">^>A"] )
            if val == "<": move.append( ["A"] )
            if val == "^": move.append( [">^A"] )
            if val == "v": move.append( [">A"] )
            if val == ">": move.append( [">>A"] )
        if self.pos == "v":
            if val == "A": move.append( ["^>A",">^A"] )
            if val == "<": move.append( ["<A"] )
            if val == "^": move.append( ["^A"] )
            if val == "v": move.append( ["A"] )
            if val == ">": move.append( [">A"] )
        if self.pos == ">":
            if val == "A": move.append( ["^A"] )
            if val == "<": move.append( ["<<A"] )
            if val == "^": move.append( ["^<A","<^A"] )
            if val == "v": move.append( ["<A"] )
            if val == ">": move.append( ["A"] )
        if self.pos == "^":
            if val == "A": move.append( [">A"] )
            if val == "<": move.append( ["v<A"] )
            if val == "^": move.append( ["A"] )
            if val == "v": move.append( ["vA"] )
            if val == ">": move.append( ["v>A",">vA"] )
        self.pos = val
        self.sequence.append(move)
        
    def move_to2(self, val):
        y,x = self.find(val)
        if y < self.y: # Move horizontal first, then vertical
            if x > self.x:
                self.sequence = self.sequence + [">" * (x-self.x)]
            else:
                self.sequence = self.sequence + ["<" * (self.x-x)]
            if y > self.y:
                self.sequence = self.sequence + ["v" * (y-self.y)]
            else:
                self.sequence = self.sequence + ["^" * (self.y-y)]
        else: # Move vertical first, then horizontal
            if y > self.y:
                self.sequence = self.sequence + ["v" * (y-self.y)]
            else:
                self.sequence = self.sequence + ["^" * (self.y-y)]
            if x > self.x:
                self.sequence = self.sequence + [">" * (x-self.x)]
            else:
                self.sequence = self.sequence + ["<" * (self.x-x)]
        self.sequence.append("A")
        self.y = y
        self.x = x
        self.pos = val

    def get_sequence(self):
        return "".join(self.sequence)


def part1():
    data = EX[:]
    total = 0
    for i in range(len(data)):
        print(data[i])

        num_keypad = NumericKeypad()
        for j in range(len(data[i])):
            instr = data[i][j]
            num_keypad.move_to(instr)
        seq1 = num_keypad.get_sequence()
        print(seq1)

        dir_keypad1 = DirectionalKeypad()
        for j in range(len(seq1)):
            instr = seq1[j]
            dir_keypad1.move_to(instr)
        seq2 = dir_keypad1.get_sequence()
        print(seq2)

        dir_keypad2 = DirectionalKeypad()
        for j in range(len(seq2)):
            instr = seq2[j]
            dir_keypad2.move_to(instr)
        seq3 = dir_keypad2.get_sequence()
        print(seq3)
        complexity = int(data[i].replace("A","")) * len(seq3)
        print(len(seq3),int(data[i].replace("A","")),complexity)
        total += complexity
        print()
    return total

"""

029A
<A^A^^>AvvvA
v<<A>>^A<A>A<AAv>A^Av<AAA>^A
v<A<AA>>^AvAA<^A>Av<<A>>^AvA^Av<<A>>^AAv<A>A^A<A>Av<A<A>>^AAAvA<^A>A

029A
<A^A>^^AvvvA
v<<A>>^A<A>AvA<^AA>A<vAAA>^A
<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A


379A: 
<v<A >>^A vA ^A <vA <A A >>^A    AvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A - answer
v<<A >>^A vA ^A v<<A >>^A A v<A<A>>^AAvAA<^A>Av<A>^AA<A>Av<A<A>>^AAAvA<^A>A - generated

"""
#  -  ^  A
#  <  v  >

# <A>Av<<A
# <A>A<AA

def part2():
    pass

if __name__=="__main__":
    start = time.time()
    result = part1()
    print(f"Part 1 result:",result)
    result = part2()
    print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


