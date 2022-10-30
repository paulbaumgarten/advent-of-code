
with open("03.txt", "r") as f:
    data = f.read().splitlines()

ones = [0,0,0,0,0,0,0,0,0,0,0,0]
zeros = [0,0,0,0,0,0,0,0,0,0,0,0]

# Count zeros and ones
for n in data:
    for i in range(len(n)):
        if n[i] == "1":
            ones[i] += 1
        else:
            zeros[i] += 1

# Form the gamma and epsilon numbers
gamma = 0
epsilon = 0
print(ones)
print(zeros)
for i in range(0,12):
    if ones[i] > zeros[i]:
        gamma += (1<<(12-i-1))
    else:
        epsilon += (1<<(12-i-1))

print(gamma, epsilon)
s1 = bin(gamma)[2:]
print(s1.rjust(12))
print(gamma * epsilon)

def get_0_1_count(nums, prefix):
    print("prefix: ",prefix)
    zeros, ones = 0, 0
    for n in nums:
        if n[0:len(prefix)] == prefix:
            print(n)
            if n[len(prefix)] == "1":
                ones += 1
            else:
                zeros += 1
    print(ones, zeros)
    return ones, zeros

nums = [int(s,2) for s in data]
print(nums)
oxygen = ""
co2 = ""
while len(oxygen) < len(data[0]):
    # Is it most common for this bit to be 0 or 1?
    ones, zeros = get_0_1_count(data, oxygen)
    if ones + zeros == 1:
        for d in data:
            if d[0:len(oxygen)] == oxygen:
                oxygen = d               
    elif ones > zeros:
        oxygen += "1"
    elif ones < zeros:
        oxygen += "0"
    else:
        oxygen += "1"
    
while len(co2) < len(data[0]):
    # Is it most common for this bit to be 0 or 1?
    ones, zeros = get_0_1_count(data, co2)
    if ones + zeros == 1:
        for d in data:
            if d[0:len(co2)] == co2:
                co2 = d               
    elif zeros < ones:
        co2 += "0"
    elif zeros > ones:
        co2 += "1"
    else:
        co2 += "0"
print(oxygen)
print(co2)
print(int(oxygen,2), int(co2,2))
print(int(oxygen,2) * int(co2,2)) # 2772000 is too low

