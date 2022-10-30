

class Board:
    def __init__(self, init_data):
        self.data = [[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]]
        for i in range(0,5):
            for j in range(0,5):
                self.data[i][j] = int(init_data[i][(j*3):(j*3)+2].lstrip())
    
    def __str__(self):
        s = ""
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])):
                s += str(self.data[i][j]).rjust(3)
            s += "\n"
        return s
    
    def play(self, num):
        # If we have the selected number, mark it as played
        check = False
        won = False
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])):
                if self.data[i][j] == num:
                    self.data[i][j] = -1
                    check = True # Don't exit loop incase the number appears more than once
        if check: # Have we won?
            # Check rows
            for i in range(0,len(self.data)):
                row = 0
                for j in range(0,len(self.data[i])):
                    row += self.data[i][j]
                if row == -5:
                    return True
            # Check columns
            for i in range(0,5):
                col = 0
                for j in range(0,5):
                    col += self.data[j][i]
                if col == -5:
                    return True
        return won
    
    def score(self):
        s = 0
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])):
                if self.data[i][j] >= 0:
                    s += self.data[i][j]
        return s
    
    def dump(self):
        print(self.data)


if __name__=="__main__":
    with open("04.txt", "r") as f:
        data = f.read().splitlines()
    
    drawn = data[0]
    drawn = [int(n) for n in drawn.split(",")]

    boards = []
    for i in range(2, len(data),6):
        boards.append(Board(data[i:i+5]))

    print("Boards loaded...")
    for i in range(len(boards)):
        boards[i].dump()
        # print(boards[i])

    n = 0
    winner = -1
    while winner == -1:
        num = drawn[n]
        print("Playing",num)
        for i in range(0, len(boards)):
            won = boards[i].play(num)
            if won:
                winner = i
        n += 1
    print("Winning board")
    boards[winner].dump()
    s = boards[winner].score()
    print(s, num) # 929 80
    print(s*num) # 74320

    print("Part 2...")
    n = 0
    lastwon = False
    while not lastwon:
        num = drawn[n]
        print("Playing",num)
        i = 0
        while i < len(boards):
            won = boards[i].play(num)
            if won:
                if len(boards) == 1:
                    lastwon = True
                else:
                    boards.pop(i)
            else:
                i += 1
        n += 1
    print("Losing board")
    boards[0].dump()
    s = boards[0].score()
    print(s, num)
    print(s*num)


