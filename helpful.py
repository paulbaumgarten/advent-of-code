### Helper functions

class Line:
    def __init__(self, x1, x2, value):
        self.x1 = x1 # Inclusive
        self.x2 = x2 # Inclusive
        self.value = value
    
    def split_line(self, point):
        if point > self.x1 and point <= self.x2:
            return [ Line(self.x1, point-1, self.value), 
                     Line(point, self.x2, self.value) ]
        else:
            return [ self ]

class Rectangle:
    def __init__(self, x1, y1, x2, y2, value):
        self.x1 = x1 # Inclusive
        self.x2 = x2 # Inclusive
        self.y1 = y1 # Inclusive
        self.y2 = y2 # Inclusive
        self.value = value
    
    def split_shape_x(self, point):
        if point > self.x1 and point <= self.x2:
            return [ Rectangle(self.x1, self.y1, point-1, self.y2, self.value), 
                     Rectangle(point, self.y1, self.x2, self.y2, self.value) ]
        else:
            return [ self ]

    def split_shape_y(self, point):
        if point > self.y1 and point <= self.y2:
            return [ Rectangle(self.x1, self.y1, self.x2, point-1, self.value), 
                     Rectangle(self.x1, point, self.x2, self.y2, self.value) ]
        else:
            return [ self ]

class Box:
    def __init__(self, x1, y1, z1, x2, y2, z2, value):
        self.x1 = x1 # Inclusive
        self.x2 = x2 # Inclusive
        self.y1 = y1 # Inclusive
        self.y2 = y2 # Inclusive
        self.z1 = z1 # Inclusive
        self.z2 = z2 # Inclusive
        self.value = value
    
    def split_shape_x(self, point):
        if point > self.x1 and point <= self.x2:
            return [ Box(self.x1, self.y1, self.z1, 
                        point-1, self.y2, self.z2,
                        self.value), 
                    Box(point, self.y1, self.z1,
                        self.x2, self.y2, self.z2,
                        self.value) ]
        else:
            return [ self ]

    def split_shape_y(self, point):
        if point > self.y1 and point <= self.y2:
            return [ Box(self.x1, self.y1, self.z1, 
                        self.x2, point-1, self.z2,
                        self.value), 
                    Box(self.x1, point, self.z1,
                        self.x2, self.y2, self.z2,
                        self.value) ]
        else:
            return [ self ]

    def split_shape_z(self, point):
        if point > self.z1 and point <= self.z2:
            return [ Box(self.x1, self.y1, self.z1, 
                        self.x2, self.y2, point-1,
                        self.value), 
                    Box(self.x1, self.y1, self.z1,
                        self.x2, self.y2, point,
                        self.value) ]
        else:
            return [ self ]

class Tesseract:
    def __init__(self, x1, y1, z1, w1, x2, y2, z2, w2, value):
        self.x1 = x1 # Inclusive
        self.x2 = x2 # Inclusive
        self.y1 = y1 # Inclusive
        self.y2 = y2 # Inclusive
        self.z1 = z1 # Inclusive
        self.z2 = z2 # Inclusive
        self.w1 = w1 # Inclusive
        self.w2 = w2 # Inclusive
        self.value = value
    
    def split_shape_x(self, point):
        if point > self.x1 and point <= self.x2:
            return [ Tesseract(self.x1, self.y1, self.z1, self.w1,
                        point-1, self.y2, self.z2, self.w2, 
                        self.value), 
                    Tesseract(point, self.y1, self.z1, self.w1,
                        self.x2, self.y2, self.z2, self.w2,
                        self.value) ]
        else:
            return [ self ]

    def split_shape_y(self, point):
        if point > self.y1 and point <= self.y2:
            return [ Tesseract(self.x1, self.y1, self.z1, self.w1,
                        self.x2, point-1, self.z2, self.w2, 
                        self.value), 
                    Tesseract(self.x1, point, self.z1, self.w1,
                        self.x2, self.y2, self.z2, self.w2,
                        self.value) ]
        else:
            return [ self ]

    def split_shape_z(self, point):
        if point > self.z1 and point <= self.z2:
            return [ Tesseract(self.x1, self.y1, self.z1, self.w1,
                        self.x2, self.y2, point-1, self.w2, 
                        self.value), 
                    Tesseract(self.x1, self.y1, point, self.w1,
                        self.x2, self.y2, self.z2, self.w2,
                        self.value) ]
        else:
            return [ self ]

    def split_shape_w(self, point):
        if point > self.w1 and point <= self.w2:
            return [ Tesseract(self.x1, self.y1, self.z1, self.w1,
                        self.x2, self.y2, self.z2, point-1, 
                        self.value), 
                    Tesseract(self.x1, self.y1, self.z1, point,
                        self.x2, self.y2, self.z2, self.w2,
                        self.value) ]
        else:
            return [ self ]

    def __repr__(self):
        return f"Tesseract from ({self.x1},{self.y1},{self.z1},{self.w1}) -> ({self.x2},{self.y2},{self.z2},{self.w2}) = {self.value}"
    
    def get_volume(self):
        return (self.x2-self.x1)*(self.y2-self.y1)*(self.z2-self.z1)*(self.w2-self.w1)


def all_permutations(pattern, values):
    """
    Will create a list of strings, where the spaces in the origin string have been replaced with every permutation of value in the options list.
    origin: An input string with spaces.
    options: A list of the various values to replace the spaces with.
    # dat = all_permutations(" / ", [0,1,2,3,4,5,6,7,8,9])
    """
    working = True
    result = [pattern]
    while working:
        working = False
        space = result[0].find(" ")
        if space >= 0:
            this_pattern = result.pop(0)
            for i in range(0, len(values)):
                result.append( this_pattern[0:space] + str(values[i]) + this_pattern[space+1:] )
            working = True
    return result

def is_in_bounds(grid, y, x):
    return (y >= 0 and x >= 0 and y < len(grid) and x < len(grid[y]))

def traverse_matrix(grid, callable):
    for y in range(0, len(grid)):
        for x in range(0, len(grid[y])):
            callable(grid, y, x)
