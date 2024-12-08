
FILE = "./2023/2023-19.txt"

TEST = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""".split("\n\n")

class Part:
    def __init__(self, st):
        st = (st[1:])[:-1]
        x,m,a,s = st.split(",")
        self.x = int(x[2:])
        self.m = int(m[2:])
        self.a = int(a[2:])
        self.s = int(s[2:])

    def total(self):
        return self.x+self.m+self.a+self.s
    

def process1(part, workflows):
    current = "in"
    while True:
        work = workflows[current]
        i = 0
        while True:
            task = work[i]
            if task[0] == "goto":
                if task[1] == "A" or task[1] == "R":
                    return task[1]
                current = task[1]
                break
            else:
                if task[2] == "<" and part[ task[1] ] < task[3]:
                    if task[4] == "A" or task[4] == "R":
                        return task[4]
                    current = task[4]
                    break
                if task[2] == ">" and part[ task[1] ] > task[3]:
                    if task[4] == "A" or task[4] == "R":
                        return task[4]
                    current = task[4]
                    break
            i += 1

def part1():
    with open(FILE, "r") as f:
        workflows_text,parts_text = f.read().split("\n\n")
    #workflows_text,parts_text = TEST
    parts = []
    workflows = {}
    # Parse parts data
    for p in parts_text.split("\n"):
        x,m,a,s = (p[1:])[:-1].split(",")
        x = int(x[2:])
        m = int(m[2:])
        a = int(a[2:])
        s = int(s[2:])
        parts.append( { "x":x, "m": m, "a": a, "s":s } )
    # Parse workflows data
    for w in workflows_text.split("\n"):
        label, rules = w.split("{")
        rules = rules[:-1].split(",")
        ruleset = []
        for r in rules:
            if r.count(":") == 1: # Is this a rule to be calculated? or a default destination?
                colon = r.index(":")
                if "<" in r:
                    operator = r.index("<")
                else:
                    operator = r.index(">")
                ruleset.append(("calc", r[0:operator], r[operator], int(r[operator+1:colon]), r[colon+1:] ))
            else:
                ruleset.append(("goto",r))
        workflows[label] = ruleset
    # Run calculations
    total = 0
    for i in range(0, len(parts)):
        result = process1(parts[i], workflows)
        if result == "A":
            total += parts[i]["x"] + parts[i]["m"] + parts[i]["a"] + parts[i]["s"]
    print(total)

def resolve_expression(workflows, exp):
    if exp == "A" or exp == "R":
        return exp
    elif ":" in exp:
        seperate = exp.find(":")
        evaluation = exp[ : seperate ]
        options = exp[ seperate+1 : ]
        comma = options.find(",")
        first = options[ : comma ]
        second = options[ comma+1 : ]
        return evaluation, resolve_expression(workflows,first), resolve_expression(workflows,second)
    else: # We have a function name to result
        exp = workflows[exp]
        seperate = exp.find(":")
        evaluation = exp[ : seperate ]
        options = exp[ seperate+1 : ]
        comma = options.find(",")
        first = options[ : comma ]
        second = options[ comma+1 : ]
        return evaluation, resolve_expression(workflows,first), resolve_expression(workflows,second)

def update_all_space(space, dimension, op, boundary, value ):
    spaces = len(space)
    i = 0
    while i < spaces:
        this_shape = space.pop(0)
        if op == ">":
            boundary += 1
        if dimension=="x":
            new_shapes = this_shape.split_shape_x(boundary)
        elif dimension=="y":
            new_shapes = this_shape.split_shape_y(boundary)
        elif dimension=="z":
            new_shapes = this_shape.split_shape_z(boundary)
        elif dimension=="w":
            new_shapes = this_shape.split_shape_w(boundary)
        if len(new_shapes) == 2:
            if op == "<":
                new_shapes[0].value = value
            elif op == ">":
                new_shapes[1].value = value
            space.append(new_shapes[0])
            space.append(new_shapes[1])
        else:
            space.append(new_shapes[0])
        i += 1
    return space

def traverse_rules(rules, x1,x2,m1,m2,a1,a2,s1,s2):
    total = 0
    if rules == "A":
        area = abs(x2-x1+1) * abs(m2-m1+1) * abs(a2-a1+1) * abs(s2-s1+1)
        print(x1,x2,m1,m2,a1,a2,s1,s2," == > ",area,"ALLOWED")
        return area
    if rules == "R":
        area = abs(x2-x1) * abs(m2-m1) * abs(a2-a1) * abs(s2-s1)
        print(x1,x2,m1,m2,a1,a2,s1,s2," == > ",area,"REJECTED")
        return 0
    if len(rules) == 3:
        #print(rules)
        expression = rules[0]
        variable = expression[0]
        operator = expression[1]
        v = int(expression[2:])
        r1, r2, = rules[1], rules[2]
        if operator == ">": # eg: m>2090
            if variable == "x":
                total += traverse_rules(r1, v+1,x2, m1,m2,  a1,a2,  s1,s2)
                total += traverse_rules(r2, x1,v,   m1,m2,  a1,a2,  s1,s2)
            if variable == "m":
                total += traverse_rules(r1, x1,x2,  v+1,m2, a1,a2,  s1,s2)
                total += traverse_rules(r2, x1,x2,  m1,v,   a1,a2,  s1,s2)
            if variable == "a":
                total += traverse_rules(r1, x1,x2,  m1,m2,  v+1,a2, s1,s2)
                total += traverse_rules(r2, x1,x2,  m1,m2,  a1,v,   s1,s2)
            if variable == "s":
                total += traverse_rules(r1, x1,x2,  m1,m2,  a1,a2,  v+1,s2)
                total += traverse_rules(r2, x1,x2,  m1,m2,  a1,a2,  s1,v)
        else: # eg: s<1351
            if variable == "x":
                total += traverse_rules(r1, x1,v-1, m1,m2,  a1,a2,  s1,s2)
                total += traverse_rules(r2, v,x2,   m1,m2,  a1,a2,  s1,s2)
            if variable == "m":
                total += traverse_rules(r1, x1,x2,  m1,v-1, a1,a2,  s1,s2)
                total += traverse_rules(r2, x1,x2,  v,m2,   a1,a2,  s1,s2)
            if variable == "a":
                total += traverse_rules(r1, x1,x2,  m1,m2,  a1,v-1, s1,s2)
                total += traverse_rules(r2, x1,x2,  m1,m2,  v,a2,   s1,s2)
            if variable == "s": 
                total += traverse_rules(r1, x1,x2,  m1,m2,  a1,a2,  s1,v-1)
                total += traverse_rules(r2, x1,x2,  m1,m2,  a1,a2,  v,s2)
        return total
    print(rules, x1,x2,m1,m2,a1,a2,s1,s2, total)
    raise Exception("What the hell am I doing here?")


def part2():
    with open(FILE, "r") as f:
        workflows_text,parts_text = f.read().split("\n\n")
    #workflows_text,parts_text = TEST
    parts = []
    workflows = {}
    # Parse workflows data
    for w in workflows_text.split("\n"):
        label, rules = w.split("{")
        rules = rules[:-1]
        workflows[label] = rules
    for k,v in workflows.items():
        print(k," => ",v)
    
    rules = resolve_expression(workflows, "in")
    print(rules)
    print()
    total = traverse_rules(rules, 1,4000,1,4000,1,4000,1,4000)
    print("total",total)

part1()
part2()

