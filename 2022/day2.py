import time
from pprint import pprint

"""
Opponent move: A for Rock, B for Paper, and C for Scissors
Responding move: X for Rock, Y for Paper, and Z for Scissors
Part 2
    X = must lose, 
    Y = must draw
    Z = must win
Scores: 
    your piece  1 for Rock, 2 for Paper, and 3 for Scissors
    + result    0 if you lost, 3 if the round was a draw, and 6 if you won
"""

start = time.time()
with open("./2022/day2.txt", "r") as f:
    data = f.read().splitlines()

demo = """A Y
B X
C Z""".splitlines()

def part1(data):
    points_available = {
        "A": { "X": 4, "Y": 8, "Z": 3 },
        "B": { "X": 1, "Y": 5, "Z": 9 },
        "C": { "X": 7, "Y": 2, "Z": 6 },
    }
    score = 0
    for turn in data:
        opponent, me = turn.split(" ")
        # print(opponent, me, points_available[opponent][me])
        score += points_available[opponent][me]
    print(score)

def part2(data):
    points_available = {
        "A": { "X": 0+3, "Y": 3+1, "Z": 6+2 },
        "B": { "X": 0+1, "Y": 3+2, "Z": 6+3 },
        "C": { "X": 0+2, "Y": 3+3, "Z": 6+1 },
    }
    score = 0
    for turn in data:
        opponent, me = turn.split(" ")
        print(opponent, me, points_available[opponent][me])
        score += points_available[opponent][me]
    print(score)

part1(data)
part2(data)
print("Execution time:",time.time()-start)
