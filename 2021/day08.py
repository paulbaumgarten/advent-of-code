import time

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
 
2 letters = digit 1 = segments --c--f-
4 letters = digit 4 = segments -bcd-f-
3 letters = digit 7 = segments a-c--f-
7 letters = digit 8 = segments abcdefg

6 letters...
* if missing part of "1"...         = digit 6 (segments ab-defg)
* if all parts of "4" within...     = digit 9 (segments abcd-fg)
* if not 6 or 9...                  = digit 0 (segments abc-efg)

5 letters...
* if all parts of "1" within...     = digit 3 (segments a-cd-fg)
* if all parts appear within "6"... = digit 5 (segments ab-d-fg)
* if not 3 or 5...                  = digit 2.

"""

# Prepare data
with open("day08.txt", "r") as f:
    data = f.read().splitlines()
data = [d.split(" | ") for d in data]
patterns = []
outputs = []
for datum in data:
    patterns.append(datum[0].split(" "))
    outputs.append(datum[1].split(" "))
print(outputs)

# Solve part 1
digits = [0,0,0,0,0,0,0,0,0,0]
for output in outputs:
    for n in output:
        if len(n) == 2: digits[1] += 1
        if len(n) == 4: digits[4] += 1
        if len(n) == 3: digits[7] += 1 
        if len(n) == 7: digits[8] += 1
print(sum(digits))


# Solve an individual row of part 2
def decode_digits(pattern):
    digits = ['X','X','X','X','X','X','X','X','X','X']
    for n in pattern:
        if len(n) == 2: digits[1] = n
        if len(n) == 4: digits[4] = n
        if len(n) == 3: digits[7] = n 
        if len(n) == 7: digits[8] = n
    # Some deductions
    while 'X' in digits:
        for n in pattern:
            # Find digit 3... if length 5 and both pats of 1 exist, it must be 3
            if len(n) == 5 and (digits[1][0] in n) and (digits[1][1] in n):
                digits[3] = n
            # Find digit 6... if length 6 and one of the parts of 1 is missing, it must be 6
            if len(n) == 6 and ((digits[1][0] not in n) or (digits[1][1] not in n)):
                digits[6] = n
            # Find digit 9... if length 6 and all parts of 4 appear in 9
            if len(n) == 6 and (digits[4][0] in n) and (digits[4][1] in n) and (digits[4][2] in n) and (digits[4][3] in n):
                digits[9] = n
            # Find digit 0... if length 6, and not the number 6 or 9, it must be 0 
            if len(n) == 6 and (digits[6] != 'X') and (digits[9] != 'X') and (n != digits[6]) and (n != digits[9]):
                digits[0] = n
            # Find digit 5... if length 5, and all parts appear in 6
            if len(n) == 5 and (digits[6] != 'X') and (n[0] in digits[6] and n[1] in digits[6] and n[2] in digits[6] and n[3] in digits[6] and n[4] in digits[6]):
                digits[5] = n
            # Find digit 2... what's left?
            if len(n) == 5 and (digits[5] != 'X') and (digits[3] != 'X') and (n != digits[5]) and (n != digits[3]):
                digits[2] = n
    for i in range(0, len(digits)):
        digits[i] = "".join(sorted(digits[i]))
    return digits

# Solve part 2
total = 0
for i in range(len(outputs)):
    pattern = decode_digits(patterns[i])
    output = outputs[i]
    for j in range(0, len(output)):
        output[j] = "".join(sorted(output[j]))
    print("pattern: ",pattern)
    print("output:  ", output)
    number = pattern.index(output[0]) * 1000 + \
        pattern.index(output[1]) * 100 + \
        pattern.index(output[2]) * 10 + \
        pattern.index(output[3])
    print("value:   ",number)
    #time.sleep(1)
    total += number

print(total)

