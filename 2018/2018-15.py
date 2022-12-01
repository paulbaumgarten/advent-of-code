import time, math

input2 = """################################
#########################.G.####
#########################....###
##################.G.........###
##################.##.......####
#################...#.........##
################..............##
######..########...G...#.#....##
#####....######.G.GG..G..##.####
#######.#####G............#.####
#####.........G..G......#...####
#####..G......G..........G....##
######GG......#####........E.###
#######......#######..........##
######...G.G#########........###
######......#########.....E..###
#####.......#########........###
#####....G..#########........###
######.##.#.#########......#####
#######......#######.......#####
#######.......#####....E...#####
##.G..#.##............##.....###
#.....#........###..#.#.....####
#.........E.E...#####.#.#....###
######......#.....###...#.#.E###
#####........##...###..####..###
####...G#.##....E####E.####...##
####.#########....###E.####....#
###...#######.....###E.####....#
####..#######.##.##########...##
####..######################.###
################################"""

input1 = """#######   
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""

class Piece:
    def __init__(self, label, hit=0):
        self.label = label
        self.hit = hit
    #def __str__(self) -> str:
    #    return self.label[0]

def print_grid(g):
    for y in range(0,len(g)):
        for x in range(0, len(g[y])):
            print(g[y][x], end="")
        print()

def get_distance(grid, origin, dest):

def part1():
    """
    All Goblins & Elf's start with 3 attack power and 200 hit points
    Rounds
        Order of player 'moves' determined by reading order position at the start of the round, ignoring how they may move during the round.
        Identify targets
        Identify each open square adjacent to each target (attacking square)
        If no open square
            Pass, no move
        If unit not currently 'in range'
            Pick closst attacking square
            Take 1 step towards it on shortest path or reading order path
        Now, if unit currently is 'in range' of a target
            Attack
            If multiple enemies adjacant, pick the 1 with the fewest hit-points (reading order tie break)
            Enemy hit_points = hit_points - my attack_power
            If hit_points <= 0, enemy dies, square becomes '.'
    """
    print("Part 1")
    battle_royale = True
    round = 0
    grid = [[ch for ch in s.strip()] for s in input1.splitlines()]
    for y in range(0,len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "#": grid[y][x] = Piece("#", 0)
            if grid[y][x] == ".": grid[y][x] = Piece(".", 0)
            if grid[y][x] == "G": grid[y][x] = Piece("goblin", 200)
            if grid[y][x] == "E": grid[y][x] = Piece("elf", 200)
    #print_grid(grid)
    while battle_royale:
        round = round + 1
        print(f"Round {round}")
        # Determine order of players
        order = []
        for y in range(0,len(grid)):
            for x in range(0, len(grid[y])):
                order.append((y,x))
        # Player turn
        for coord in order:
            i_am = grid[coord[0]][coord[1]]
            # Identify target opportunities
            targets = []
            print(grid[0][0].label)
            for y in range(0,len(grid)):
                for x in range(0, len(grid[y])):
                    if grid[y][x].label != "#" and grid[y][x].label != "." and grid[y][x].label != i_am.label:
                        targets.append((y,x))
            print(targets)
            # Identify open and reachable adjacent squares to targets
            closest_idx = 0
            closest_distance = math.inf
            for i in range(targets):
                distance = get_distance(grid, coord, targets[i])
                if distance < closest_distance and distance >= 0:
                    closest_distance = distance
                    closest_idx = i
            

            exit()


start = time.time()
part1()
print("Time taken ",time.time()-start)

