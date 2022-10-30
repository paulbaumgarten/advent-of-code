# Day 21

#### PART 1

players = [4, 8] # Test input
players = [1, 6] # Live input: Player 1 starting position: 1, Player 2 starting position: 6
scores = [0, 0]

class Dice1:
    def __init__(self):
        self.n = 1
        self.rolls = 0
    def next(self):
        out = self.n
        self.rolls += 1
        self.n += 1
        if self.n > 100:
            self.n = 1
        return out
    def get_rolls(self):
        return self.rolls

def part1():
    dice = Dice1()
    move = 0
    while scores[0] < 1000 and scores[1] < 1000:
        if move % 6 < 3:
            rolled = dice.next()
            players[0] += rolled
            while players[0] > 10:
                players[0] = players[0] - 10
            if move % 6 == 2:
                scores[0] += players[0]
        else:
            rolled = dice.next()
            players[1] += rolled
            while players[1] > 10:
                players[1] = players[1] - 10
            if move % 6 == 5:
                scores[1] += players[1]
        print(rolled, players, scores)
        move += 1
    if scores[0] >= 1000:
        print(scores[1] * dice.get_rolls())
    else:
        print(scores[0] * dice.get_rolls())

#part1()
#exit()

#### PART 2
# Part 2 test data
# Player 1 wins in 444'356'092'776'315 universes, 444 trillion
# player 2 wins in 341'960'390'180'808 universes, 341 trillion
# Player 1 wins in 444356092776315 universes, 
# player 2 wins in 341960390180808 universes

# Initialise - number of places to advance on the board for each universe created by each turn 
moves_to_make = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            moves_to_make.append(i+j+k)
moves_to_make.sort()
print("moves_to_make",moves_to_make)
# moves_to_make [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]

p1_win = 0
p2_win = 0
# In position p1=4 and p2=8, at p1 with 0 points and p2 with 0 points, there is 1 game
state = {
    (1, 6, 0, 0) : 1
}
for round in range(0,15):
    new_state = {}
    for positions, copies in state.items():
        p1_position, p2_position, p1_points, p2_points = positions
        for dice1 in moves_to_make: # Player 1 move
            p1_new_position = 1+( p1_position + dice1 -1) % 10
            p1_new_score = p1_points + p1_new_position
            if p1_new_score >= 21:
                p1_win += copies
            else:
                for dice2 in moves_to_make: # Player 2 move
                    p2_new_position = 1+( p2_position + dice2 -1) % 10
                    p2_new_score = p2_points + p2_new_position
                    if p2_new_score >= 21:
                        p2_win += copies
                    else:
                        # Search existing cache of states to see if this already exists, if so increment it
                        new_key = (p1_new_position, p2_new_position, p1_new_score, p2_new_score)
                        #print(f"Player1 position {p1_position} with {p1_points} points and player2 position {p2_position} with {p2_points} points")
                        #print(f" - Player 1 rolled a {dice1}, player 2 rolled a {dice2}")
                        #print(f" - Player1 moves to {p1_new_position} with {p1_new_score} points and player2 moves to {p2_new_position} with {p2_new_score} points")
                        if new_key in new_state.keys():
                            new_state[new_key] += copies
                        # Cache of states doesn't have this yet, create it
                        else:
                            new_state[new_key] = copies
    state = new_state
    print()
    print("round",round, "contains",len(state),"states")
print(state)

print(f"# Player 1 wins in {p1_win} universes") 
print(f"# Player 2 wins in {p2_win} universes") 



"""
ok.... i spent so many hours on all these different attempts, I'm keeping them here! hahaha

works for p2 but not player 1 :(

moves_to_make = []
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            moves_to_make.append(i+j+k)
moves_to_make.sort()
print("moves_to_make",moves_to_make)
# moves_to_make [3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 6, 5, 6, 7, 6, 7, 8, 5, 6, 7, 6, 7, 8, 7, 8, 9]

p1_win = 0
p2_win = 0
# In position p1=4 and p2=8, at p1 with 0 points and p2 with 0 points, there is 1 game
state = {
    (4, 8, 0, 0) : 1
}

for round in range(0,15):
    new_state = {}
    for positions, copies in state.items():
        p1_position, p2_position, p1_points, p2_points = positions
        for dice1 in moves_to_make: # Player 1 move
            for dice2 in moves_to_make: # Player 2 move
                p1_new_position = 1+( p1_position + dice1 -1) % 10
                p2_new_position = 1+( p2_position + dice2 -1) % 10
                p1_new_score = p1_points + p1_new_position
                p2_new_score = p2_points + p2_new_position
                if p1_new_score >= 21:
                    p1_win += copies
                elif p2_new_score >= 21:
                    p2_win += copies
                else:
                    # Search existing cache of states to see if this already exists, if so increment it
                    new_key = (p1_new_position, p2_new_position, p1_new_score, p2_new_score)
                    #print(f"Player1 position {p1_position} with {p1_points} points and player2 position {p2_position} with {p2_points} points")
                    #print(f" - Player 1 rolled a {dice1}, player 2 rolled a {dice2}")
                    #print(f" - Player1 moves to {p1_new_position} with {p1_new_score} points and player2 moves to {p2_new_position} with {p2_new_score} points")
                    if new_key in new_state.keys():
                        new_state[new_key] += copies
                    # Cache of states doesn't have this yet, create it
                    else:
                        new_state[new_key] = copies
    state = new_state
    print()
    print("round",round)
print(state)

print(f"# Player 1 wins in {p1_win} universes") 
print(f"# Player 2 wins in {p2_win} universes") 








---------------------
p1 = {
    ( 4, 0 ) : 1
}
p2 = {
    ( 8, 0) : 1
}
loop_count = 0
while len(p1.keys()) + len(p2.keys()) > 0:
    loop_count += 1
    print(f"Loop { loop_count}: with {len(p1)} * {len(p2)} * { len(moves_to_make) } = { len(p1) * len(p2) * len(moves_to_make) } items to process")
    #if loop_count == 3:
    #    print("p1",p1)
    #    print("p2",p2)
    #    #break
    p1_new = {}
    p2_new = {}
    for p1k, p1v in p1.items():
        for p2k, p2v in p2.items():
            p1_old_pos = p1k[0]
            p1_old_points = p1k[1]
            p2_old_pos = p2k[0]
            p2_old_points = p2k[1]

            for m in moves_to_make:
                p1_new_pos = 1 + ( p1_old_pos + m -1 ) % 10
                p1_new_points = p1_old_points + p1_new_pos
                p2_new_pos = 1 + ( p2_old_pos + m -1 ) % 10
                p2_new_points = p2_old_points + p2_new_pos
                if p1_new_points >= 21:
                    p1_win += p1v
                elif p2_new_points >= 21:
                    p2_win += p2v
                else:
                    if (p1_new_pos, p1_new_points ) in p1_new.keys():
                        p1_new[(p1_new_pos, p1_new_points)] += m * p1v
                    else:
                        p1_new[(p1_new_pos, p1_new_points)] = m * p1v
                    if (p2_new_pos, p2_new_points) in p2_new.keys():
                        p2_new[(p2_new_pos, p2_new_points)] += m * p1v
                    else:
                        p2_new[(p2_new_pos, p2_new_points)] = m * p2v
    p1 = p1_new
    p2 = p2_new
    print(p1_win, p2_win)


def print_scores(name, round, points):
    print(f"Player {name} round {round} -------------------")
    print("         ", end="")
    for position in range(1,11):
        print(f"{position:8}", end=" ")
    print()
    print("         ", end="")
    for position in range(1,11):
        print(f"--------", end=" ")
    print()
    for score in range(1,22):
        print(f"{score:8}", end=" ")
        for position in range(1,11):
            print(f"{points[score][position]:8}", end=" ")
        print()
    print()


# How many universes contain each score for this player
p1_scores = [[ 0 for n in range(11)] for m in range(22) ]
p2_scores = [[ 0 for n in range(11)] for m in range(22) ]


# Play first round
for move in moves_to_make:
    p1_lands_on = 1 + (p1_start + move - 1) % 10
    p2_lands_on = 1 + (p2_start + move - 1) % 10
    p1_points = p1_start + p1_lands_on
    p2_points = p2_start + p2_lands_on
    p1_scores[ p1_points ][ p1_lands_on ] = move
    p2_scores[ p2_points ][ p2_lands_on ] = move

round = 0
print_scores("p1", round, p1_scores)
print()
exit()

round = 1
p1_win = 0
p2_win = 0
# Play second round
while sum(p1_universes_of_score[1:22]) > 0 and sum(p2_universes_of_score[1:22]) > 0:
    p1_temp = [0] * 32
    p2_temp = [0] * 32
    for i in range(0, 22):
        p1_current_universe_count = p1_universes_of_score[i] # Number of universes with this score
        p2_current_universe_count = p2_universes_of_score[i] # Number of universes with this score
        for move in moves_to_make:
            p1_points_to_add = 1+(i+move-1)%10
            p2_points_to_add = 1+(i+move-1)%10
            if i+p1_points_to_add >= 21:
                p1_win += p1_current_universe_count
            elif i+p2_points_to_add >= 21:
                p2_win += p2_current_universe_count
            else:
                p1_temp[ i+p1_points_to_add ] += p1_current_universe_count
                p2_temp[ i+p2_points_to_add ] += p2_current_universe_count
    p1_universes_of_score = p1_temp.copy()
    p2_universes_of_score = p2_temp.copy()
    print("p1_universes_of_score",round,p1_universes_of_score, sum(p1_universes_of_score))
    print("p2_universes_of_score",round,p2_universes_of_score, sum(p2_universes_of_score))
    print()
    round +=1
print(p1_win, p2_win)
"""



"""
player 1 cache
4 = 1 ... 4
5 = 1 ... 4+1
6 = 2 ... 4+1+1, 4+2
7 = c(6)+c(5)+c(4) = 2+1+1 =  4 ... 4+1+1+1, 4+3, 4+2+1, 4+1+2
8 = c(7)+c(6)+c(5) = 4+3+2 = 9
9 = c(8)+c(7)+c(6) = 9+4+2 = 15


move number
0       board       4
        score       0
1       board       5,                                  6,                                  7
        scores      5,                                  6,                                  7
2       board       6           7           8           7           8           9           8           9           10
        scores      11,         12,         13          13,         14,         15          15,         16,         17
3       board       7  8  9     8  9  10    9  10 1     8  9  10    9  10 1     10 1  2     9  10 1     10  1  2    1  2  3
        scores      18 19 20    20 21 22    22 23 14    21 22 23    23 24 15    25 16 17    24 25 16    26  17 18   18 19 20


3 rolls = this change in the board = then add the board value to the score
1 2 3
2 3 4   3 4 5   4 5 6
3 4 5   4 5 6   5 6 7   4 5 6   5 6 7   6 7 8   5 6 7   6 7 8   7 8 9


"""


