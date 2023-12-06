
FILE = "./2023/2023-05.txt"

def parse():
    with open(FILE, "r") as f:
        data = f.read().splitlines()
    seeds = [int(n) for n in data[0][7:].split(" ")]
    # the destination range start, the source range start, and the range length
    # unmapped means destination <-- source
    labels = {
        "seed-to-soil" : "seed_soil",
        "soil-to-fertilizer" : "soil_fert",
        "fertilizer-to-water": "fert_water",
        "water-to-light" : "water_light",
        "light-to-temperature" : "light_temp",
        "temperature-to-humidity" : "temp_hum",
        "humidity-to-location" : "hum_loc"
    }
    inf = {
        "seed_soil": [],
        "soil_fert": [],
        "fert_water": [],
        "water_light": [],
        "light_temp": [],
        "temp_hum": [],
        "hum_loc": []
    }
    current = ""
    for line in range(2,len(data)):
        if "map:" in data[line]:
            t = data[line][:-5]
            current = labels[t]
            print(f"Parsing {current}")
        elif data[line] != "":
            dest, src, leng = data[line].split(" ")
            dest, src, leng = int(dest), int(src), int(leng)
            inf[current].append({"dest":dest, "src":src, "leng":leng})
    return seeds, labels, inf

def part1():
    seeds, labels, inf = parse()
    print(inf)
    locations = []
    for seed in seeds:
        loc = -1
        item = seed
        for k,v in inf.items():
            # Process this conversion
            for lookups in v:
                orig = item
                if item >= lookups["src"] and item <= lookups["src"]+lookups["leng"]:
                    diff = item-lookups["src"]
                    item = lookups["dest"]+diff
                    print(f"  - {k} from {orig} to {item}")
                    break            
        print(f"seed {seed} has location {item}")
        locations.append(item)
    # Find the lowest location value
    print(min(locations))

def part2_demo():
    seeds, labels, inf = parse()
    min_location = -1
    print(seeds)
    seeds2 = []
    for s in range(0,len(seeds),2):
        fr = seeds[s]
        stop = seeds[s]+seeds[s+1]
        seeds2.append({"src":fr, "leng":stop})
        print(f"Processing seed range from {fr} to {stop}")
        for seed in range(fr, stop):
            #print(f"Seed {seed}...")
            loc = -1
            item = seed
            for k,v in inf.items():
                # Process this conversion
                for lookups in v:
                    orig = item
                    if item >= lookups["src"] and item <= lookups["src"]+lookups["leng"]:
                        diff = item-lookups["src"]
                        item = lookups["dest"]+diff
                        #print(f"  - {k} from {orig} to {item}")
                        break            
            #print(f"seed {seed} has location {item}")
            if min_location < 0 or item < min_location:
                min_location = item
    # Find the lowest location value
    print(min_location)

def part2():
    seeds, labels, inf = parse()
    # Convert the data
    rounds = []
    this_round = [] # tuple: from (bottom of range), from (top of range), diff
    #for s in range(0,len(seeds),2):
    #    this_round.append((seeds[s], seeds[s]+seeds[s+1], seeds[s]))
    #rounds.append(this_round)

    for k,v in inf.items():
        # Process this conversion
        this_round = [] # tuple: from (bottom of range), from (top of range), diff
        for mapping_set in v:
            this_round.append((mapping_set['src'], mapping_set['src']+mapping_set['leng'], mapping_set['dest']-mapping_set['src']))
        rounds.append(this_round)
    #print(rounds)

    # Progress
    current_ranges=[(79, 79+14), (55, 55+13)] # [(79, 93), (55, 68)]
    i =1
    for round in rounds: # Each set of values for a round (eg: seed to soil)
        next_range = []
        print("Round #",i, "range set ",round," current range",current_ranges)
        i+=1
        for current in current_ranges: # The seeds range
            dealt_with = False
            for range_set in round: # ( from_bottom, from_max_diff, diff )
                if   current[0] < range_set[0] and current[0]<range_set[1] and current[1] < range_set[1] and current[1] > range_set[0]:
                    next_range.append(( current[0], range_set[0] ))
                    next_range.append(( range_set[0]+range_set[2], current[1]+range_set[2] ))
                    #next_range.append(( range_set[0]+1, current[1] ))
                    dealt_with = True
                elif current[0] > range_set[0] and current[0]<range_set[1] and current[1] < range_set[1] and current[1] > range_set[0]:
                    next_range.append(( current[0]+range_set[2], current[1]+range_set[2] ))
                    #next_range.append(( current[0], current[1] ))
                    dealt_with = True
                elif current[0] < range_set[0] and current[0]<range_set[1] and current[1] > range_set[1] and current[1] > range_set[0]:
                    next_range.append(( current[0], range_set[0] ))
                    next_range.append(( range_set[0]+range_set[2], range_set[1]+range_set[2] ))
                    #next_range.append(( range_set[0]+1, range_set[1] ))
                    next_range.append(( range_set[1], current[1] ))
                    dealt_with = True
                elif current[0] > range_set[0] and current[0]<range_set[1] and current[1] > range_set[1] and current[1] > range_set[0]:
                    next_range.append(( current[0]+range_set[2], range_set[1]+range_set[2] ))
                    #next_range.append(( current[0], range_set[1] ))
                    next_range.append(( range_set[1], current[1] ))
                    dealt_with = True
            if not dealt_with:
                next_range.append(( current[0], current[1] ))
        while len(current_ranges)>0:
            current_ranges.pop()
        while len(next_range)>0:
            current_ranges.append(next_range.pop())    
        print("current_ranges",current_ranges)
    starting_values = []
    for r in current_ranges:
        starting_values.append(r[0])
    print(min(starting_values))

#part1()
part2_demo()
#part2()

