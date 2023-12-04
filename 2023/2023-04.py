
FILE = "./2023/2023-04.txt"

def part1(): #907th
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    total = 0
    for i in range(0, len(data)):
        card, game = data[i].split(": ")
        win_str, play_str = game.split(" | ")
        win_arr = win_str.split(" ")
        play_arr = play_str.split(" ")
        win = []
        play = []
        for w in win_arr:
            if w is not None and w.isnumeric():
                win.append(int(w))
        for p in play_arr:
            if p is not None and p.isnumeric():
                play.append(int(p))
        print(win,"  ",play)
        points = 0
        for i in play:
            if i in win:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total += points
    print(total)

def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    cards = {}
    # Parse the file into something nicer
    for i in range(0, len(data)):
        card, game = data[i].split(": ")
        card = int(card[5:])
        win_str, play_str = game.split(" | ")
        win_arr = win_str.split(" ")
        play_arr = play_str.split(" ")
        win = []
        play = []
        for w in win_arr:
            if w is not None and w.isnumeric():
                win.append(int(w))
        for p in play_arr:
            if p is not None and p.isnumeric():
                play.append(int(p))
        cards[card] = {"win":win, "play":play}
    print(cards)    
    # Let's play
    # How many matching numbers for each card
    for card, game in cards.items():
        matching_numbers = 0
        for p in game["play"]:
            if p in game["win"]:
                matching_numbers += 1
        cards[card]["matching"] = matching_numbers
        cards[card]["instances"] = 1 # We start with one instance of each card
    print(cards)    
    # Award bonus copies of cards
    for card, game in cards.items():
        won = game["matching"]
        for i in range(0, won):
            cards[card+1+i]["instances"] += cards[card]['instances']
    # Count instances
    total = 0
    for card, game in cards.items():
        print(f"Card {card} has {game['instances']} instances")
        total += game['instances']
    print("Total",total)

#part1()
part2()

