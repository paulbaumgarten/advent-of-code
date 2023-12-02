# Advent of code 2023 day 1

with open("2023-1.txt", "r") as f:
    data = f.read().splitlines()

def part1(data):
    total = 0
    for i in range(0, len(data)):
        line = data[i]
        first = -1
        last = -1
        for j in range(0, len(line)):
            if line[j].isnumeric():
                if first < 0:
                    first = int(line[j])
                last = int(line[j])
        total += first*10+last
    print(total)

def part2(data):
    num = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    for i in range(0, len(data)):
        line = data[i]
        first = -1
        last = -1
        for j in range(0, len(line)):
            # Check digits
            if line[j].isnumeric():
                print(line[j], end=" ")
                if first < 0:
                    first = int(line[j])
                last = int(line[j])
            # Check words
            for k in range(0,len(num)): # Check each word
                if len(line) >= j+len(num[k]): # If enough length remaining for this word
                    if line[j:j+len(num[k])] == num[k]: # Is this word at location j? 
                        if first < 0:
                            first = k
                        last = k
        total += first*10+last
        print()
    print(total)

part1()
part2()
