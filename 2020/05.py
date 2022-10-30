

def decode_seat(seat):
    rowcode = seat[:7]
    colcode = seat[7:]
    low = 0
    high = 128
    for i in rowcode:
        mid = (low + high) // 2
        if i == "F":
            high = mid
        else:
            low = mid
    row = low
    low = 0
    high = 8
    for i in colcode:
        mid = (low + high) // 2
        if i == "L":
            high = mid
        else:
            low = mid
    return row,low,row*8+low


with open("05.txt", "r") as f:
    content = f.read().splitlines()

max = 0
for seat in content:
    row, col, id = decode_seat(seat)
    print(f"{seat} is row {row} and column {col} and id {id}")
    if id > max:
        max = id
print("Max found was ",max)

