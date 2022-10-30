"""
--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

Your puzzle answer was 2289.

--- Part Two ---
As soon as people start to arrive, you realize your mistake. People don't just care about adjacent seats - they care about the first seat they can see in each of those eight directions!

Now, instead of considering just the eight immediately adjacent seats, consider the first seat in each of those eight directions. For example, the empty seat below would see eight occupied seats:

.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
The leftmost empty seat below would only see one empty seat, but cannot see any of the occupied ones:

.............
.L.L.#.#.#.#.
.............
The empty seat below would see no occupied seats:

.##.##.
#.#.#.#
##...##
...L...
##...##
#.#.#.#
.##.##.
Also, people seem to be more tolerant than you expected: it now takes five or more visible occupied seats for an occupied seat to become empty (rather than four or more from the previous rules). The other rules still apply: empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor never changes.

Given the same starting layout as above, these new rules cause the seating area to shift around as follows:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
Again, at this point, people stop shifting around and the seating area reaches equilibrium. Once this occurs, you count 26 occupied seats.

Given the new visibility method and the rule change for occupied seats becoming empty, once equilibrium is reached, how many seats end up occupied?

Your puzzle answer was 2059.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

from pprint import pprint
import time

def get_seat(seats, x,y):
    if 0 <= y < len(seats) and 0<= x < len(seats[0]):
        return seats[y][x]
    else:
        return 'X'

def get_adjacent_seat_stats(seats, x,y):
    data = get_seat(seats, x-1, y-1) + \
        get_seat(seats, x, y-1) + \
        get_seat(seats, x+1, y-1) + \
        get_seat(seats, x-1, y) + \
        get_seat(seats, x+1, y) + \
        get_seat(seats, x-1, y+1) + \
        get_seat(seats, x, y+1) + \
        get_seat(seats, x+1, y+1)
    empty = data.count(".")
    occupied = data.count("#")
    return empty, occupied

def get_seeable_seat_in_direction_of(seats, fromx, fromy, dx, dy):
    seat = get_seat(seats, fromx+dx, fromy+dy)
    if seat == '.':
        return get_seeable_seat_in_direction_of(seats, fromx+dx, fromy+dy, dx, dy)
    else:
        return seat

def get_seeable_seat_stats(seats, x,y):
    data = get_seeable_seat_in_direction_of(seats, x, y, -1, -1) + \
        get_seeable_seat_in_direction_of(seats, x, y, 0, -1) + \
        get_seeable_seat_in_direction_of(seats, x, y, 1, -1) + \
        get_seeable_seat_in_direction_of(seats, x, y, -1, 0) + \
        get_seeable_seat_in_direction_of(seats, x, y, 1, 0) + \
        get_seeable_seat_in_direction_of(seats, x, y, -1, 1) + \
        get_seeable_seat_in_direction_of(seats, x, y, 0, 1) + \
        get_seeable_seat_in_direction_of(seats, x, y, 1, 1)
    empty = data.count(".")
    occupied = data.count("#")
    return empty, occupied

def problem2_complete_round(seats):
    changes = 0
    seats2 = []
    for y in range(len(seats)):
        row = ""
        for x in range(len(seats[y])):
            current = get_seat(seats, x,y)
            empty, occupied = get_seeable_seat_stats(seats,x,y)
            if current == 'L' and occupied == 0:
                row += "#"
                changes += 1
            elif current == '#' and occupied >= 5:
                row += 'L'
                changes += 1
            else:
                row += current
        seats2.append(row)
    # copy back to original list
    for i in range(len(seats)):
        seats[i] = seats2[i]
    return changes

def problem1_complete_round(seats):
    changes = 0
    seats2 = []
    for y in range(len(seats)):
        row = ""
        for x in range(len(seats[y])):
            current = get_seat(seats, x,y)
            empty, occupied = get_adjacent_seat_stats(seats,x,y)
            if current == 'L' and occupied == 0:
                row += "#"
                changes += 1
            elif current == '#' and occupied >= 4:
                row += 'L'
                changes += 1
            else:
                row += current
        seats2.append(row)
    # copy back to original list
    for i in range(len(seats)):
        seats[i] = seats2[i]
    return changes

def problem1(seats):
    print("\n\nStatus of seats...")
    pprint(seats)
    changes = problem1_complete_round(seats)
    print("\n\nStatus of seats...")
    pprint(seats)
    while changes > 0:
        changes = problem1_complete_round(seats)
        print("\n\nStatus of seats...")
        pprint(seats)
    # Safety
    for i in range(4):
        changes = problem1_complete_round(seats)
    # How many seats end up occupied?
    occ = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                occ += 1
    print(f"There are {occ} occupied seats")

def problem2(seats):
    print("\n\nStatus of seats...")
    pprint(seats)
    changes = problem2_complete_round(seats)
    print("\n\nStatus of seats...")
    pprint(seats)
    while changes > 0:
        changes = problem2_complete_round(seats)
        print("\n\nStatus of seats...")
        pprint(seats)
    # Safety
    for i in range(4):
        changes = problem2_complete_round(seats)
    # How many seats end up occupied?
    occ = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                occ += 1
    print(f"There are {occ} occupied seats")


with open("11.txt", "r") as f:
    content = f.read().splitlines()

#problem1(content)
problem2(content)
