import math, random, numpy, os, re, copy, time

DEMO = "125 17"
LIVE = "0 44 175060 3442 593 54398 9 8101095"

### Today's problem

def get_data():
    return LIVE

def apply_stone_rules(stone):
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if stone == 0: 
        return 1, None
    # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    l = len(str(stone)) # abcd
    if l > 1 and l % 2 == 0:
        return int(str(stone)[0:l//2]), int(str(stone)[l//2:])
    # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
    return stone * 2024, None

def part1(raw):
    stones = DEMO[:]
    stones = raw[:]
    stones = [int(n) for n in stones.split(" ")]
    iterations = 25
    for i in range(0, iterations):
        for s in range(len(stones)-1, -1, -1):
            s1, s2 = apply_stone_rules(stones[s])
            stones[s] = s1
            if s2 != None:
                stones.insert(s+1, s2)
        #print("iteration ",i,"stones:\n => ",stones)
    return len(stones)

def part2(raw):
    memo = {}
    stones = DEMO[:]
    stones = raw[:]
    stones = {int(n):1 for n in stones.split(" ")}
    iterations = 75
    print(stones)
    for i in range(0, iterations):
        #print(i, stones)
        new_stones = {}
        for stone, qty in stones.items():
            s1, s2 = apply_stone_rules(stone)
            if not s1 in new_stones.keys():
                new_stones[s1] = 0
            new_stones[s1] += qty
            if s2 != None:
                if not s2 in new_stones.keys():
                    new_stones[s2] = 0
                new_stones[s2] += qty
        stones = new_stones
    #print(i, stones)
    total = 0
    for k,v in stones.items():
        total += v
    return total

if __name__=="__main__":
    start = time.time()
    #result = part1(get_data())
    #print(f"Part 1 result:",result) # 197157
    #if result:
    result = part2(get_data())
    print("Part 2 result:",result)
    finish = time.time()
    print(f"Time taken: {(finish-start):.2f} seconds")


