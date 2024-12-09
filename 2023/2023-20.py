import math, random, numpy, os, re, copy, time

class FlipFlop: # prefix %
    def __init__(self,name):
        self.state = False
        self.name = name
    
    def receive(self, pulse):
        if not False:
            self.state = not self.state
    
    def get_state(self):
        return self.state
    
    def __repr__(self):
        return self.name

class Conjunction: # prefix &
    def __init__(self,name):
        self.name=name
        self.inputs = []
        self.input_states = []

    def set_input(self, input, state):
        self.inputs.append(input)
        self.input_states.append(False)
    
    def receive(self, input, new_state):
        for x in range(len(self.inputs)):
            if input == self.inputs[i]:
                self.input_states[i] = new_state

    def get_state(self):
        result = True
        for state in self.input_states:
            result = result and state
        if result:
            return False
        else:
            return True

    def __repr__(self):
        return self.name

class Broadcast:
    def __init__(self,name):
        self.name=name
        self.destinations = []

    def add_destination(self, dest):
        self.destinations.append(dest)
    
    def receive(self, pulse):
        for x in range(0, len(self.destinations)):
            self.destinations[x].receive(pulse)

    def __repr__(self):
        return self.name

DEMO = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a""".splitlines()

def get_data():
    path_parts = __file__.split(os.path.sep)
    filename_parts = path_parts[-1].split(".")
    data_path = os.path.sep.join(path_parts[:-1])+os.path.sep+filename_parts[0]+".txt"
    print(f"Reading {data_path}")
    with open(data_path,"r",encoding="utf-8") as f:
        data = f.read().splitlines()
    return data

### Today's problem

def part1(raw):
    data = DEMO[:]
    modules = {}
    for line in data:
        module,recipiants = line.split(" -> ")
        

def part2(raw):
    pass

if __name__=="__main__":
    start = time.time()
    result = part1(get_data())
    print(f"Part 1 result:",result)
    if result:
        result = part2(get_data())
        print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


