"""
[({(<(())[]>[[{[]{<()<>>

{([(<{}[<>[]}>{[]{[(<()> - Expected ], but found } instead.
[[<[([]))<([[{}[[()]]] - Expected ], but found ) instead.
[{[{({}]{}}([{[{{{}}([] - Expected ), but found ] instead.
[<(<(<(<{}))><([]([]() - Expected >, but found ) instead.
<{([([[(<>()){}]>(<<{{ - Expected ], but found > instead.

): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points

"""

with open("day10.txt", "r") as f:
    data = f.read().splitlines()

openers = ['(', '[', '{', '<']
closers = [')', ']', '}', '>']
worth = [3, 57, 1197, 25137]
worth2 = [1, 2, 3, 4]

# Solve an individual problem
def part1(instr):
    points = 0
    place = 0
    chunksopen = 0
    chunks = []
    while place < len(instr):
        if instr[place] in openers:
            chunksopen += 1
            chunks.append(instr[place])
        elif instr[place] in closers:
            chunksopen -= 1
            v = chunks.pop()
            if openers.index(v) != closers.index(instr[place]): # Mis-match
                points = worth[closers.index(instr[place])]
        place += 1
    print(instr," points: ",points)
    return points

# Iterate through each problem
points = 0
for instr in data:
    points += part1(instr)
print(points)

# Ignore the lines with "corruption"
i = 0
while i < len(data):
    if part1(data[i]) > 0:
        data.pop(i)
    else:
        i += 1
print("---- part 2 ----")

def part2(instr):
    points = 0
    place = 0
    chunksopen = 0
    chunks = []
    while place < len(instr):
        if instr[place] in openers:
            chunksopen += 1
            chunks.append(instr[place])
        elif instr[place] in closers:
            chunksopen -= 1
            v = chunks.pop()
        place += 1
    # Incomplete instructions will mean items remain on the stack
    while len(chunks) > 0:
        v = chunks.pop()
        points = (points*5) + worth2[ openers.index(v) ]
    print(instr," points: ",points)
    return points

# Iterate through each problem
points = []
for instr in data:
    points.append(part2(instr))
points = sorted(points)
print(points[ len(points)//2 ])




