# Day 16
# Binary parsing

"""
* Each packet may contain other packets
* Each packet 
    - 1st 3 bits = packet version (number)
    - 2nd 3 bits = type ID (number)
* Type ID == 4  --> Literal value
    - if 1st bit = 1, read next 4 bits
    - if 1st bit = 0, end of literal, ignore until end of character of the string being parsed
    - put all the literals together to make a number
* Type ID != 4  --> Operator
* Length type ID == 0 
    - Next 15 bits = a number total size of the sub-packets this packet contains
* Length type ID == 1
    - Next 11 bits = the number of sub-packets this packet contains
    

def part1(inp):
    b = bytearray.fromhex(inp)
    pos = 0
    while pos < len(b):
        print(b[pos])
        ver = (b[pos] & 0b1110000) >> 5
        typeid = (b[pos] & 0b00011100) >> 2
        print("ver",ver, "typeid",typeid)
        if typeid != 4:
            length_typeid = (b[pos] & 0b00000010) >> 1

        pos += 1

# 00111000
part1("38006F45291200")
#inp = input()
"""
