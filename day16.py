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
"""

def hextobinarystring(inp):
    ret = ""
    for i in range(0, len(inp), 2):
        byte = bin(int(inp[i:i+2], base=16))[2:].rjust(8, '0')
        ret += byte
    return ret

def part1_literal(data):
    # 01234
    i = 0
    val = 0
    print(data)
    while data[i] == "1":
        val = val * 16
        print(data[i+1:i+5])
        val += int(data[i+1:i+5], base=2)
        i += 5
    if data[i] == "0":
        val = val * 16
        print(data[i+1:i+5])
        val += int(data[i+1:i+5], base=2)
        i += 5
    return val, i

def part1(data):
    print(data)
    position = 0
    ver = int(data[0:3], base=2)
    typeid = int(data[3:6], base=2)
    if typeid == 4:
        val, until = part1_literal(data[6:])
        print(val)
        position = until
    if typeid != 4:
        length_typeid = int(data[6:7], base=2)
        if length_typeid == 0:
            subpacket_length = int(data[7:8+15], base=2)
            position = 8+15
        else:
            subpacket_number = int(data[7:8+11], base=2)
            position = 8+11
 
# 00111000
data = [
    "D2FE28",
    "38006F45291200",
    "005410C99A9802DA00B43887138F72F4F652CC0159FE05E802B3A572DBBE5AA5F56F6B6A4600FCCAACEA9CE0E1002013A55389B064C0269813952F983595234002DA394615002A47E06C0125CF7B74FE00E6FC470D4C0129260B005E73FCDFC3A5B77BF2FB4E0009C27ECEF293824CC76902B3004F8017A999EC22770412BE2A1004E3DCDFA146D00020670B9C0129A8D79BB7E88926BA401BAD004892BBDEF20D253BE70C53CA5399AB648EBBAAF0BD402B95349201938264C7699C5A0592AF8001E3C09972A949AD4AE2CB3230AC37FC919801F2A7A402978002150E60BC6700043A23C618E20008644782F10C80262F005679A679BE733C3F3005BC01496F60865B39AF8A2478A04017DCBEAB32FA0055E6286D31430300AE7C7E79AE55324CA679F9002239992BC689A8D6FE084012AE73BDFE39EBF186738B33BD9FA91B14CB7785EC01CE4DCE1AE2DCFD7D23098A98411973E30052C012978F7DD089689ACD4A7A80CCEFEB9EC56880485951DB00400010D8A30CA1500021B0D625450700227A30A774B2600ACD56F981E580272AA3319ACC04C015C00AFA4616C63D4DFF289319A9DC401008650927B2232F70784AE0124D65A25FD3A34CC61A6449246986E300425AF873A00CD4401C8A90D60E8803D08A0DC673005E692B000DA85B268E4021D4E41C6802E49AB57D1ED1166AD5F47B4433005F401496867C2B3E7112C0050C20043A17C208B240087425871180C01985D07A22980273247801988803B08A2DC191006A2141289640133E80212C3D2C3F377B09900A53E00900021109623425100723DC6884D3B7CFE1D2C6036D180D053002880BC530025C00F700308096110021C00C001E44C00F001955805A62013D0400B400ED500307400949C00F92972B6BC3F47A96D21C5730047003770004323E44F8B80008441C8F51366F38F240"
]
which = int(input("Which?"))
print(part1(hextobinarystring(data[which])))

