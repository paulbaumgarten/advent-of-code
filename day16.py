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
    
# 00111000
#inp = input()
"""

def literal(inp, position=0):
    value = 0
    while inp[position] == "1":
        value = value * 16 + int(inp[position+1:position+5], base=2)
        position += 5
    value = value * 16 + int(inp[position+1:position+5], base=2)
    position += 5
    return value, position

def packet(b, pos=0):
    print("Processing packet:",b)
    ver = int(b[pos:pos+3], base=2)
    print("Version:",ver)
    packet_type_id = int(b[pos+3:pos+6], base=2)
    pos +=6
    if packet_type_id == 4:
        val, pos = literal(b, pos)
        print("Literal value ",val)
        return pos
    else:
        length_type_id = int(b[pos])
        pos+=1
        if length_type_id == 0:
            subpacket_length = int(b[pos:pos+15], base=2)
            print("Subpacket length:",subpacket_length)
            pos+=15
            pos += packet(b[pos:pos+subpacket_length])
            return pos
        elif length_type_id == 1:
            subpacket_qty = int(b[pos:pos+11], base=2)
            pos+=11
            for i in range(subpacket_qty):
                pos = packet(b, pos)

data = bin(int("38006F45291200", base=16))[2:]
while len(data) % 4 != 0:
    data = "0" + data
print(data)
packet(data)

