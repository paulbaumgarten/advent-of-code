
def part1(): #907th
    with open("./2023/2023-02.txt", "r") as f:
        data = f.read().splitlines()
    
    possible = 0
    max_r = 12
    max_g = 13
    max_b = 14
    for i in range(0, len(data)):
        id, game = data[i].split(": ")
        id = int(id.split(" ")[1])
        rounds = game.split("; ")
        ok = True
        for j in range(0, len(rounds)):
            colors_used = rounds[j].split(", ")
            for k in range(0, len(colors_used)):
                qty,color = colors_used[k].split(" ")
                qty=int(qty)
                if color=="blue":
                    if qty > max_b:
                        ok = False
                elif color=="red":
                    if qty > max_r:
                        ok = False
                elif color=="green":
                    if qty > max_g:
                        ok = False
        if ok:
            possible += id
    print(possible)

def part2():
    with open("./2023/2023-02.txt", "r") as f:
        data = f.read().splitlines()
    
    power_sum = 0
    for i in range(0, len(data)):
        id, game = data[i].split(": ")
        id = int(id.split(" ")[1])
        rounds = game.split("; ")
        min_r, min_g, min_b = 0,0,0
        for j in range(0, len(rounds)):
            colors_used = rounds[j].split(", ")
            for k in range(0, len(colors_used)):
                qty,color = colors_used[k].split(" ")
                qty=int(qty)
                if color=="blue":
                    if qty > min_b:
                        min_b = qty
                elif color=="red":
                    if qty > min_r:
                        min_r = qty
                elif color=="green":
                    if qty > min_g:
                        min_g = qty
        game_power = min_g * min_b * min_r
        power_sum += game_power
    print(power_sum)

part1()
part2()

