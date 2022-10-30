# Day 20

# dot = dark = 0, hash = lit = 1

# Part 1
# 5402 is too low, 5232 too high, 5229 is correct
# Part 2
# 35757 is too high

with open("day20.txt", "r") as f:
    fdata = f.read().splitlines()

filter = fdata[0]
img = [[1 if ch == '#' else 0 for ch in line] for line in fdata[2:]]

def print_image(img):
    for y in range(0, len(img)):
        for x in range(0, len(img[y])):
            print(f"{ '.' if img[y][x] == 0 else '#' }", end="")
        print()
    print()

def expand_image(img):
    out = []
    expand_by = 8 # Must be divisble by 2
    for a in range(0, expand_by, 2):
        out.append([0 for _ in range(0, len(img[0])+expand_by)])
    for y in range(0, len(img[0])):
        row = [n for n in img[y]]
        for a in range(0, expand_by, 2):
            row.insert(0, 0)
        out.append(row)
        for a in range(0, expand_by, 2):
            row.append(0)
    for a in range(0, expand_by, 2):
        out.append([0 for _ in range(0, len(img[0])+expand_by)])
    return out

def cell(img, y, x):
    if y < 0 or y >= len(img) or x < 0 or x >= len(img[y]):
        return "0"
    else:
        return str(img[y][x])
        
def filter_image(img):
    out = [[img[y][x] for x in range(len(img[y]))] for y in range(len(img))]
    for y in range(0, len(img)):
        for x in range(0, len(img[y])):
            val = cell(img,y-1,x-1)+cell(img,y-1,x)+cell(img,y-1,x+1)+\
                    cell(img,y,x-1)+cell(img,y,x)+cell(img,y,x+1)+\
                    cell(img,y+1,x-1)+cell(img,y+1,x)+cell(img,y+1,x+1)
            dec = int(val, base=2)
            # print(val ,dec, y,x,filter[dec])
            new_pixel = filter[dec]
            out[y][x] = 0 if new_pixel=='.' else 1
    return out

print_image(img)
total = sum([sum([n for n in row]) for row in img])
print(total)
diffs = []
for i in range(0,50,2):
    print(f"img size is {len(img)} rows x {len(img[0])} columns")
    img = expand_image(img)
    #print_image(img)
    img = filter_image(img)
    #print_image(img)
    img = filter_image(img)
    #print_image(img)
    print(f"img size is {len(img)} rows x {len(img[0])} columns")

    # Hackery needed for live data ensues...
    img[0][0] = 0
    img[0][len(img[0])-1] = 0
    img[len(img[0])-1][0] = 0
    # End of hackery section
    
    new_total = sum([sum([n for n in row]) for row in img])
    diffs.append(new_total-total)
    print(new_total, (new_total-total))
    total = new_total
print(diffs)

