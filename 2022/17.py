import time, math
from pprint import pprint

"""
####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

7 units wide
appearance = left edge is 2 spaces in from left wall
appearance = its bottom edge is three units above the highest rock in the room 

alternate between
* sideways push
* down one

If any movement would cause any part of the rock to move into the walls, floor, or a stopped rock, the movement instead does not occur.

"""

# Points from shapes no longer moving
matrix = []

class Shape:
    def __init__(self, shape_number, y):
        # points are (y,x) where y increases up, x increases right
        self.landed = False
        self.y = y
        self.x = 2
        if shape_number==0:
            self.shape = [(0,0), (0,1), (0,2), (0,3)]
            self.width = 4
            self.height = 1
        elif shape_number==1:
            self.shape = [(0,1), (1,0), (1,1), (1,2), (2,1)]
            self.width = 3
            self.height = 3
        elif shape_number==2:
            self.shape = [(0,0), (0,1), (0,2), (1,2), (2,2)]
            self.width = 3
            self.height = 3
        elif shape_number==3:
            self.shape = [(0,0), (1,0), (2,0), (3,0)]
            self.width = 1
            self.height = 4
        elif shape_number==4:
            self.shape = [(0,0), (0,1), (1,0), (1,1)]
            self.width = 2
            self.height = 2
        self.points = []
        for p in self.shape:
            self.points.append((p[0]+self.y, p[1]+self.x))
    
    def land(self):
        self.landed = True
        return self.points

    def down(self, matrix):
        ok = True
        for p in self.points:
            y,x = p
            if (y-1,x) in matrix:
                ok = False
                self.land()
        for p in self.points:
            y,x = p
            if y-1 < 0:
                ok = False
                self.land()
        if ok:
            for p in range(0, len(self.points)):
                self.points[p] = (self.points[p][0]-1, self.points[p][1])
        return ok

    def sideways(self, matrix, move):
        dx = 1 if move==">" else -1
        # Check we won't hit another rock
        for p in self.points:
            y,x = p
            if (y,x+dx) in matrix:
                return False
        # Check we won't hit a wall
        for p in range(0, len(self.points)):
            if (self.points[p][1]+dx) < 0 or (self.points[p][1]+dx) > 6:
                return False
        # Make the move
        for p in range(0, len(self.points)):
            self.points[p] = (self.points[p][0], self.points[p][1]+dx)
        return True


def draw(shape):
    board = [['.' for x in range(7)] for y in range(10)]
    for y in range(0, len(board)):
        for x in range(0,7):
            if (y,x) in shape.points:
                board[y][x] = "#"
            elif (y,x) in matrix:
                board[y][x] = "@"
            else:
                board[y][x] = '.'
    for y in range(len(board)-1,-1,-1):
        print("|" + "".join(board[y]) + "|")
    print("+-------+")

def part1(data):
    side_move = 0
    next_rock_number = 0
    start_y = 3
    for rock in range(2022):
        # Create rock
        rock = Shape( next_rock_number, start_y )
        #draw(rock)
        next_rock_number = (next_rock_number + 1) % 5

        # while rock hasn't stopped
        while not rock.landed:
            # sideways shift
            rock.sideways(matrix, data[ side_move ])
            side_move = (side_move + 1) % len(data)

            # downwards shift
            ok = rock.down(matrix)
            if not ok:
                rock.land()
                continue

            #draw(rock)
        if rock.landed:
            for p in rock.points:
                matrix.append(p)
                if start_y < p[0]+4:
                    start_y = p[0]+4
        #draw(rock)
    # How many units tall after 2022 rounds?
    return start_y-3

def part2(data):
    side_move = 0
    next_rock_number = 0
    start_y = 3
    for r in range(1000000000000): # 1 000 000 000 000
        if r % 100000 == 0:
            print(r / 10000000000,"%" ,time.time()-start,"seconds",len(matrix),"matrix items")
        # Create rock
        rock = Shape( next_rock_number, start_y )
        #draw(rock)
        next_rock_number = (next_rock_number + 1) % 5

        # while rock hasn't stopped
        while not rock.landed:
            # sideways shift
            rock.sideways(matrix, data[ side_move ])
            side_move = (side_move + 1) % len(data)

            # downwards shift
            ok = rock.down(matrix)
            if not ok:
                rock.land()
                continue

            #draw(rock)
        if rock.landed:
            for p in rock.points:
                matrix.append(p)
                if start_y < p[0]+4:
                    start_y = p[0]+4
            delete_from = -1
            for y in range(rock.points[0][0], rock.points[0][0]+4):
                row_blocked = True
                for x in range(0,7):
                    if (y,x) not in matrix:
                        row_blocked = False
                if row_blocked:
                    delete_from = y
            if delete_from > 1:
                #print(f"After rock {r}. Deleting from row {delete_from}")
                i = 0
                while i < len(matrix):
                    if matrix[i][0] < delete_from:
                        matrix.pop(i)
                    else:
                        i+=1

        #draw(rock)
    # How many units tall after 2022 rounds?
    return start_y-3

def parse(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data

start = time.time()
data = parse("./2022/day 17 input.txt")
#print(part1(data))
print(part2(data))
print("Execution time:",time.time()-start)
