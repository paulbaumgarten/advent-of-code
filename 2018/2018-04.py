# 2018 Day 4

with open("2018-04.txt", "r") as f:
    data = f.read().splitlines()
data = sorted(data)
# print("\n".join(data))

guards = {}

# Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?

current = -1
sleep_start = 0
awake = True
processed = 0
for item in data:
    print(item)
    processed += 1
    #if processed > 13:
    #    break
    y=int(item[1:5])
    m=int(item[6:8])
    d=int(item[9:11])
    h=int(item[12:14])
    n=int(item[15:17])
    if item[19:24] == "Guard":
        if not awake:
            guards[current]["events"] += 1
            guards[current]["total sleep"] += 60-sleep_start
            for i in range(sleep_start, 60):
                guards[current]["minutes"][i] += 1
        current = int(item[26:].split(" ")[0])
        if current not in guards.keys():
            guards[current] = { 
                "events": 0, 
                "total sleep": 0,
                "minutes": [0 for i in range(0,60)] 
            }
    elif item[19:] == "falls asleep":
        if h == 23:
            print("Falling asleep before midnight\n   ",item)
        sleep_start = n
        awake = False
    elif item[19:] == "wakes up":
        if not awake:
            guards[current]["events"] += 1
            guards[current]["total sleep"] += n-sleep_start
            for i in range(sleep_start, n):
                guards[current]["minutes"][i] += 1
        awake = True

# Find the guard with the most sleep events
x = None
for k,v in guards.items():
    print(k," = ",guards[k])
    if x is None or guards[k]["total sleep"] > guards[x]["total sleep"]:
        x = k
print("Guard with most sleep\n", x,' = ',guards[x])
print("Guard most asleep times:")
worst_minute = 0
for i in range(0, 60):
    if guards[x]["minutes"][i] > guards[x]["minutes"][worst_minute]:
        worst_minute = i
print("Worst minute: ",worst_minute)
print("Part 1 = ", x * worst_minute)

# Part 2
guard = 0
minute = 0
val = None
for k,v in guards.items():
    for i in range(0, 60):
        if val is None or val < guards[k]["minutes"][i]:
            val = guards[k]["minutes"][i]
            guard = k
            minute = i
print("Guard ",guard,"Minute",minute,"Value",val,"Answer",guard*minute)


