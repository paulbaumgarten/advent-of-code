
def part1():
    non_symbols = ['.','0','1','2','3','4','5','6','7','8','9']
    total = 0
    with open("./2023/2023-03.txt", "r") as f:
        data = f.read().splitlines()
    for y in range(0, len(data)):
        data[y] = list(data[y])
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            if data[y][x].isnumeric(): # Start of a number
                # Find the length of the number
                l = 1
                while x+l < len(data[y]) and data[y][x+l].isnumeric():
                    l += 1
                num = data[y][x:x+l]
                print("Found ",num)
                # Check adjacents
                use_number = False
                for i in range(x-1, x+l+1):
                    if i > 0 and i < len(data[y]):
                        if y > 0:
                            if data[y-1][i] not in non_symbols:
                                use_number = True
                        if y < len(data)-1:
                            if data[y+1][i] not in non_symbols:
                                use_number = True
                if x > 1 and data[y][x-1] not in non_symbols:
                    use_number = True
                if x+l < len(data[y])-1 and data[y][x+l] not in non_symbols:
                    print(data[y][x+l+1])
                    use_number = True
                # Remove the number from further consideratio
                for i in range(0, l):
                    data[y][x+i] = '.'
                if use_number:
                    num = int("".join(num))
                    print("Using ",num)
                    total += num
    print(total)


def get_number(d, y, x):
    num = d[y][x]
    i=1
    while d[y][x-i].isnumeric():
        num = d[y][x-i] + num
        i += 1
    i=1
    while d[y][x+i].isnumeric():
        num = num + d[y][x+i]
        i += 1
    return int(num)

def part2():
    total = 0
    with open("./2023/2023-03.txt", "r") as f:
        data = f.read().splitlines()
    # Simplify boundary checking by adding spare '.' around the array
    for y in range(0, len(data)):
        data[y] = list(data[y])
    data2 = [['.' for n in range(0,len(data[y])+2)] for r in range(0,len(data)+2)]
    for y in range(0, len(data)):
        for x in range(0, len(data[y])):
            data2[y+1][x+1] = data[y][x]
    # Now get to work
    for y in range(0, len(data2)):
        for x in range(0, len(data2[y])):
            if data2[y][x] == "*": # Start of a gear
                ratio = False
                n1 = 0
                n2 = 0
                # Is there a ratio to calculate?
                pattern = [False,False,False,False,False,False,False,False]
                pattern[0] = data2[y-1][x-1].isnumeric()
                pattern[1] = data2[y-1][x].isnumeric()
                pattern[2] = data2[y-1][x+1].isnumeric()
                pattern[3] = data2[y][x-1].isnumeric()
                pattern[4] = data2[y][x+1].isnumeric()
                pattern[5] = data2[y+1][x-1].isnumeric()
                pattern[6] = data2[y+1][x].isnumeric()
                pattern[7] = data2[y+1][x+1].isnumeric()
                if pattern[0] and not pattern[1] and pattern[2]: # Up left and right
                    ratio = True
                    n1 = get_number(data2, y-1,x-1)
                    n2 = get_number(data2, y-1,x+1)
                if pattern[5] and not pattern[6] and pattern[7]: # Down left and right
                    ratio = True
                    n1 = get_number(data2, y+1,x-1)
                    n2 = get_number(data2, y+1,x+1)
                if (pattern[0] or pattern[1] or pattern[2]) and (pattern[3] or pattern[4]): # Up and middle
                    if pattern[0]:
                        n1 = get_number(data2,y-1,x-1)
                    elif pattern[1]:
                        n1 = get_number(data2,y-1,x)
                    elif pattern[2]:
                        n1 = get_number(data2,y-1,x+1)
                    if pattern[3]:
                        n2 = get_number(data2,y,x-1)
                    elif pattern[4]:
                        n2 = get_number(data2,y,x+1)
                    ratio = True
                if (pattern[5] or pattern[6] or pattern[7]) and (pattern[3] or pattern[4]): # Down and middle
                    if pattern[5]:
                        n1 = get_number(data2,y+1,x-1)
                    elif pattern[6]:
                        n1 = get_number(data2,y+1,x)
                    elif pattern[7]:
                        n1 = get_number(data2,y+1,x+1)
                    if pattern[3]:
                        n2 = get_number(data2,y,x-1)
                    elif pattern[4]:
                        n2 = get_number(data2,y,x+1)
                    ratio = True
                if pattern[3] and pattern[4]: # Left and right
                    ratio = True
                    n1 = get_number(data2, y,x-1)
                    n2 = get_number(data2, y,x+1)
                if (pattern[0] or pattern[1] or pattern[2]) and (pattern[5] or pattern[6] or pattern[7]): # Up and down
                    if pattern[0]:
                        n1 = get_number(data2,y-1,x-1)
                    elif pattern[1]:
                        n1 = get_number(data2,y-1,x)
                    elif pattern[2]:
                        n1 = get_number(data2,y-1,x+1)
                    if pattern[5]:
                        n2 = get_number(data2,y+1,x-1)
                    elif pattern[6]:
                        n2 = get_number(data2,y+1,x)
                    elif pattern[7]:
                        n2 = get_number(data2,y+1,x+1)
                    ratio = True
                if ratio:
                    print(n1,n2,n1*n2)
                    total += n1*n2
    print(total)

#part1()
part2()

