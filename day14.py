# Day 14
# Extended Polymerization - Exponential sequence growth

import time

with open("day14.txt", "r") as f:
    data = f.read().splitlines()

# Set up the data
sequence = data[0]
pairs = [a.split(" -> ") for a in data[2:]]
pairs = {s[0]:s[1] for s in pairs}
print(sequence)
counts = {}
for letter in pairs.values():
    counts[letter] = 0

# Task 1
def part1(depth):
    sequence = data[0]
    for letter in sequence:
        if letter in counts.keys():
            counts[letter] += 1
        else:
            counts[letter] = 1
    for i in range(depth):
        new_seq = ""
        for p in range(1, len(sequence)):
            pair = sequence[p-1:p+1]
            new_seq += sequence[p-1] + pairs[pair]
            counts[pairs[pair]] += 1
        sequence = new_seq + sequence[p]
        print(i, counts)
        print(sequence)
    print(counts)

# Task 2
def part2_fail(pair, depth_to_go):
    # THIS APPROACH DIDN"T WORK. TOO SLOW.
    # Time estimate was 190 days
    if len(pair) >= 2:
        insert = pairs[pair]
        counts[insert] += 1
        if depth_to_go > 1:
            part2(pair[0]+insert, depth_to_go-1)
            part2(insert+pair[1], depth_to_go-1)

def part2(sequence, generations):
    """
    Basic premise:
    The problem worked ok for 10 to 20 generations (see the failed function above) and then became too slow... so: why can't i just work out the totals for 10 generations, save them, and then add them to the totals of a fresh 10 generations... and so on
    From there it turned into this... that calculates for 1 generation, and then from the 2nd to the requested number of generations, it finds out how many letters would be created by each pair by looking them up for one generation and then adding the occurrances of the previous.
    Total time to execute < 1 second
    """
    # WORKED!!
    # Build the data empty structure...
    # [ generation ][ letter_pair ] = { letter: count, letter: count, letter: count }
    generational_pair_counts = []
    for i in range(generations):
        pair_counts = {}
        for k,v in pairs.items():
            pair_counts[k] = counts.copy()
            pair_counts[k][v] = 1
        generational_pair_counts.append(pair_counts)
    print(generational_pair_counts)
    # Populate the structure
    print("Populating the structure")
    for i in range(1,generations):
        # Add the pair_counts for the two pairs from the previous generation
        for k,v in generational_pair_counts[i].items():
            # k is the current pair, eg: NN
            # v is all the values of the counts that pair produces at this number of generations in
            letter_spawned = pairs[k]
            pair1 = k[0]+letter_spawned
            pair2 = letter_spawned+k[1]
            pair1_counts = generational_pair_counts[i-1][pair1]
            pair2_counts = generational_pair_counts[i-1][pair2]
            for letter,count in pair1_counts.items():
                generational_pair_counts[i][k][letter] += count
            for letter,count in pair2_counts.items():
                generational_pair_counts[i][k][letter] += count
        print("generation",i, generational_pair_counts[i])
    # Now traverse the sequence
    print("Traversing the sequence")
    final_counts = counts.copy()
    for i in range(0, len(sequence)-1):
        pair = sequence[i:i+2]
        for letter,count in generational_pair_counts[generations-1][pair].items():
            final_counts[letter] += count
        final_counts[sequence[i]] += 1
    final_counts[sequence[len(sequence)-1]] += 1
    print(final_counts)
    # Find the min,max
    m = max(final_counts.values())
    n = min(final_counts.values())
    print(m-n)

def part2_better(sequence, generations):
    pair_counts = {k:0 for k,v in pairs.items()}
    # Load the initial pair counts from the sequence
    for i in range(0, len(sequence)-1):
        pair = sequence[i:i+2]
        pair_counts[pair] += 1
    # Run through all pairs for generation number of times, incrementing the pairs they spawn
    for i in range(1, generations+1):
        new_pairs = []
        for pair,count in pair_counts.items():
            if count > 0:
                new_letter = pairs[ pair ]
                new_pairs.append((pair[0] + new_letter, count))
                new_pairs.append((new_letter + pair[1], count))
                pair_counts[pair] -= count # Remove this pair as it is being broken up
        for j in range(0, len(new_pairs)):
            new_pair, count = new_pairs[j]
            pair_counts[ new_pair ] += count
    # Create letter counts
    for pair, count in pair_counts.items():
        counts[pair[0]] += count
    counts[sequence[-1]] += 1
    print(pair_counts)
    print(counts)

start = time.time()

# part1(4)

#for p in range(0, len(sequence)-1):
#    print(f"p:{p} {(time.time()-start)}")
#    part2(sequence[p:p+2], 25)

# part2(sequence, 10)

part2_better(sequence, 40)


m = max(counts.values())
n = min(counts.values())
finish = time.time()
print(counts)
print(m-n)
print(finish-start)
