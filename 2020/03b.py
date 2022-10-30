"""
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

def process(rows, right=1, down=1):
    column = 0
    trees = 0
    for row in range(0, len(rows), down):
        if column >= len(rows[row]):
            column = column % len(rows[row])
        ch = rows[row][column]
        if ch == "#":
            trees += 1
        column += right
    print(f"right {right} down {down} = trees {trees}")
    return trees

with open("03.txt","r") as f:
    rows = f.read().splitlines()
"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""
a = process(rows, 1, 1)
b = process(rows, 3, 1)
c = process(rows, 5, 1)
d = process(rows, 7, 1)
e = process(rows, 1, 2)
print(a*b*c*d*e)

