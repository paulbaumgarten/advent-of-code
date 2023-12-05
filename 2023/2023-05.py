
FILE = "./2023/2023-05-test.txt"

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

#part1()
part2_demo()

