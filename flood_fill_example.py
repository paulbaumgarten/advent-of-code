
def load_grid(filename="flood_fill_example.txt"):
    with open(filename,"r") as f:
        grid = f.read().splitlines()
    for y in range(0, len(grid)):
        grid[y] = list(grid[y])
    return grid

def flood_fill_stack(grid, y=0, x=0):
    h, w = len(grid), len(grid[0])
    stack = [(y,x)]
    visit_number = 0
    while len(stack) != 0:
        y,x = stack.pop()
        grid[y][x] = str(visit_number)
        visit_number += 1
        if (y,x) == (9,9):
            return grid
        if y > 0 and grid[y-1][x] == '.':
            stack.append((y-1,x))
        if y < h-1 and grid[y+1][x] == '.':
            stack.append((y+1,x))
        if x > 0 and grid[y][x-1] == '.':
            stack.append((y,x-1))
        if x < w-1 and grid[y][x+1] == '.':
            stack.append((y,x+1))

visit_number_r = 0
def flood_fill_recursive(grid, y=0, x=0, visit_number=0):
    global visit_number_r
    h, w = len(grid), len(grid[0])
    grid[y][x] = str(visit_number_r)
    visit_number_r+=1
    if (y,x) == (9,9):
        return grid
    if y > 0 and grid[y-1][x] == '.':
        flood_fill_recursive(grid,y-1,x,visit_number+1)
    if y < h-1 and grid[y+1][x] == '.':
        flood_fill_recursive(grid,y+1,x,visit_number+1)
    if x > 0 and grid[y][x-1] == '.':
        flood_fill_recursive(grid,y,x-1,visit_number+1)
    if x < w-1 and grid[y][x+1] == '.':
        flood_fill_recursive(grid,y,x+1,visit_number+1)
    

def print_grid(grid):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            if grid[y][x] == "#":
                print("##",end=" ")
            else:
                print(grid[y][x].rjust(2,'0'),end=" ")
        print()

grid = load_grid()
#flood_fill_stack(grid)
flood_fill_recursive(grid)
print_grid(grid)

