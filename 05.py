import time

class Line:
    def __init__(self, init_data):
        xy1,xy2 = init_data.split(" -> ")
        x1,y1 = xy1.split(",")
        x2,y2 = xy2.split(",")
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)
    
    def __repr__(self):
        return (self.x1, self.y1, self.x2, self.y2)

    def __str__(self):
        return str((self.x1, self.y1, self.x2, self.y2))
    
    def is_hoizontal(self):
        return self.y1 == self.y2
    
    def is_vertical(self):
        return self.x1 == self.x2
    
    def is_horizontal_or_vertical(self):
        return self.is_hoizontal() or self.is_vertical()
    
    def is_diagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2 and abs(self.x1-self.x2)==abs(self.y1-self.y2)

# Read input data
start = time.time()

with open("05.txt", "r") as f:
    data = f.read().splitlines()

# Create array of line objects
lines = []
for d in data:
    lines.append(Line(d))

# Determine size of matrix
maxx, maxy = 0, 0
for line in lines:
    maxx = max(maxx, line.x1, line.x2)
    maxy = max(maxy, line.y1, line.y2)

# Create matrix
grid = []
for i in range(0, maxy+1):
    row = []
    for j in range(0, maxx+1):
        row.append(0)
    grid.append(row)

# Plot each line onto the grid
for l in lines:
    if l.is_hoizontal():
        if l.x1 < l.x2:
            for x in range(l.x1, l.x2+1):
                grid[l.y1][x] += 1
        else:
            for x in range(l.x1, l.x2-1, -1):
                grid[l.y1][x] += 1
    if l.is_vertical():
        if l.y1 < l.y2:
            for y in range(l.y1, l.y2+1):
                grid[y][l.x1] += 1
        else:
            for y in range(l.y1, l.y2-1, -1):
                grid[y][l.x1] += 1
    if l.is_diagonal():
        #print(l)
        dx,dy = 1,1
        if l.x1 > l.x2: dx = -1
        if l.y1 > l.y2: dy = -1
        size = abs(l.x1-l.x2)
        x = l.x1
        y = l.y1
        while x != l.x2:
            grid[y][x] += 1
            y += dy
            x += dx
        grid[y][x] += 1 # One more to do when it is equal to the end point

# Print grid
#for i in range(0, len(grid)):
#    print(grid[i])

# Count points >= 2
points = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] >= 2:
            points += 1
print(points)
print(time.time() - start)