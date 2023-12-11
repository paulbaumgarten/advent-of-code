# Day 7: Camel Cards

TEST = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()

FILE = "./2023/2023-07.txt"

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_KIND = 3
FULL_HOUSE = 4
FOUR_KIND = 5
FIVE_KIND = 6


def first_stronger1(h1, h2):
    def get_hand_value(hand):
        uniques = {}
        for i in range(0, len(hand)):
            if hand[i] in uniques.keys():
                uniques[hand[i]] += 1
            else:
                uniques[hand[i]] = 1
        if len(uniques.keys()) == 1:
            return FIVE_KIND
        if len(uniques.keys()) == 5:
            return HIGH_CARD
        if len(uniques.keys()) == 4:
            return ONE_PAIR
        if len(uniques.keys()) == 3:
            # two pair + 1, or 3 kind + 2?
            if max(uniques.values()) == 3:
                return THREE_KIND
            else:
                return TWO_PAIR
        if len(uniques.keys()) == 2:
            # full house, or 4 kind + 1?
            if max(uniques.values()) ==4:
                return FOUR_KIND
            else:
                return FULL_HOUSE

    ranks = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    if get_hand_value(h1) > get_hand_value(h2):
        return True
    elif get_hand_value(h1) < get_hand_value(h2):
        return False
    else:
        for i in range(0, len(h1)):
            if h1[i] != h2[i]:
                if ranks.index(h1[i]) < ranks.index(h2[i]):
                    return True
                else:
                    return False
    print(f"ERROR - first_stronger doesn't generate result for {h1} and {h2}")
    exit()
            
def first_stronger2(h1, h2):
    def get_hand_value(hand):
        uniques = {}
        jokers = hand.count("J")
        hand = hand.replace("J","")
        for i in range(0, len(hand)):
            if hand[i] in uniques.keys():
                uniques[hand[i]] += 1
            else:
                uniques[hand[i]] = 1

        if len(uniques.keys()) <= 1:
            return FIVE_KIND

        elif len(uniques.keys()) == 2: # aaaab, aaabb, aaabJ, aabbJ, aabJJ, abJJJ
            count_of_most_common = max(uniques.values())
            if jokers == 3 or jokers == 2:
                return FOUR_KIND
            elif jokers == 1:
                if count_of_most_common == 3:
                    return FOUR_KIND
                else:
                    return FULL_HOUSE
            else:
                if count_of_most_common == 4:
                    return FOUR_KIND
                else:
                    return FULL_HOUSE

        elif len(uniques.keys()) == 3: # aaabc, aabbc, aabcJ, abcJJ
            count_of_most_common = max(uniques.values())
            if jokers == 1 or jokers == 2:
                return THREE_KIND
            if count_of_most_common == 3:
                return THREE_KIND
            return TWO_PAIR

        elif len(uniques.keys()) == 4: # aabcd, abcdJ
            return ONE_PAIR

        elif len(uniques.keys()) == 5: # abcde
            return HIGH_CARD
    
    ranks = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    if get_hand_value(h1) > get_hand_value(h2):
        return True
    elif get_hand_value(h1) < get_hand_value(h2):
        return False
    else:
        for i in range(0, len(h1)):
            if h1[i] != h2[i]:
                if ranks.index(h1[i]) < ranks.index(h2[i]):
                    return True
                else:
                    return False
    print(f"ERROR - first_stronger doesn't generate result for {h1} and {h2}")
    exit()
            
def part1():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    # Sort into lowest to highest hands
    for i in range(0, len(data)-1):
        for j in range(0, len(data)-i-1):
            print(data[j])
            hand1, bid1 = data[j].split(" ")
            hand2, bid2 = data[j+1].split(" ")
            if first_stronger1(hand1, hand2):
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
    # Calculate winnings
    total = 0
    for i in range(0, len(data)):
        hand, bid = data[i].split(" ")
        bid = int(bid)
        total = total + (i+1)*bid
    print(total)


def part2():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    #data = TEST
    # Sort into lowest to highest hands
    for i in range(0, len(data)-1):
        for j in range(0, len(data)-i-1):
            hand1, bid1 = data[j].split(" ")
            hand2, bid2 = data[j+1].split(" ")
            if first_stronger2(hand1, hand2):
                tmp = data[j]
                data[j] = data[j+1]
                data[j+1] = tmp
    # Calculate winnings
    total = 0
    for i in range(0, len(data)):
        hand, bid = data[i].split(" ")
        bid = int(bid)
        total = total + (i+1)*bid
    print(total)
    
#part1()
part2()

