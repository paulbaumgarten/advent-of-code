with open("01.txt", "r") as f:
    data = f.read().splitlines()
for i in range(len(data)):
    data[i] = int(data[i])
for i in range(len(data)):
    for j in range(i, len(data)):
        for k in range(j, len(data)):
            if data[i]+data[j]+data[k] == 2020:
                print(data[i],data[j],data[k],data[i]*data[j]*data[k])
