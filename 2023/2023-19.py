
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


class BT:
    def __init__(self, label, val):
        self.label = label
        self.val = val
        self.left = None
        self.right = None

def build_tree(workflows, node):
    for rule in node.val:


def part2():
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
    # Create tree
    root = BT("in", workflows["in"])
    build_tree(workflows, root)
    
part1()
part2()

