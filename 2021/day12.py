# Day 12
# Path finding

indata = [
    """start-A
start-b
A-c
A-b
b-d
A-end
b-end""",
    """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""",
    """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""",
"""start-YA
ps-yq
zt-mu
JS-yi
yq-VJ
QT-ps
start-yq
YA-yi
start-nf
nf-YA
nf-JS
JS-ez
yq-JS
ps-JS
ps-yi
yq-nf
QT-yi
end-QT
nf-yi
zt-QT
end-ez
yq-YA
end-JS"""
]

import time, json

# Solutions: 10, 19, 226, unknown

def visit(graph, location, path_to_here=[]):
    paths = 0
    if location == 'end':
        print(path_to_here)
        return 1
    else:
        for next_stop in graph[location]:
            if next_stop != "start":
                if next_stop.isupper() or (next_stop not in path_to_here):
                    print(path_to_here)
                    path_to_here.append(next_stop)
                    paths += visit(graph, next_stop, path_to_here)
                    path_to_here.pop()
        return paths

def visit2(graph, location, small_visit=False, path_to_here=[]):
    paths = 0
    if location == 'end':
        print(path_to_here)
        return 1
    else:
        for next_stop in graph[location]:
            if next_stop != "start":
                if next_stop.isupper() or (small_visit and (next_stop not in path_to_here)):
                    #print(path_to_here)
                    path_to_here.append(next_stop)
                    paths += visit2(graph, next_stop, small_visit, path_to_here)
                    path_to_here.pop()            
                elif (not small_visit):
                    if next_stop in path_to_here:
                        small_visit = True
                    #print(path_to_here)
                    path_to_here.append(next_stop)
                    paths += visit2(graph, next_stop, small_visit, path_to_here)
                    small_visit = False
                    path_to_here.pop()
        return paths

def builddata(data):
    output = {}
    pairs = [line.split("-") for line in data.splitlines()]
    for i in range(len(pairs)):
        if pairs[i][0] not in output.keys():
            output[pairs[i][0]] = []
        if pairs[i][1] not in output.keys():
            output[pairs[i][1]] = []
        if pairs[i][1] not in output[pairs[i][0]]:
            output[pairs[i][0]].append(pairs[i][1])
        if pairs[i][0] not in output[pairs[i][1]]:
            output[pairs[i][1]].append(pairs[i][0])
    return output

g = builddata(indata[3])
print(json.dumps(g, indent=3))
result = visit2(g, 'start')
print(result)

