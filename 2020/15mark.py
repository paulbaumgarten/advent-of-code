mem = dict()

def search(num, cur):
    if not num in mem.keys(): return 0
    return max(0, cur - mem[num])

ln = [11,18,0,20,1,7,16]
nums = [int(x) for x in ln] + [-1] * (30000000 - len(ln))

for i in range(len(nums)):
    if i % 1000000 == 0:
        print(i)
    if nums[i] == -1: 
        nums[i] = search(nums[i-1], i-1)

    if i != 0:
        mem[nums[i-1]] = i - 1

print(nums[len(nums) - 1])
