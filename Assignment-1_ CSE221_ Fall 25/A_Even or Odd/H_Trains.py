N = int(input())
trains = []
 
for idx in range(N):
    line = input().strip()
    parts = line.split()
    name = parts[0]
    time = parts[-1]
    trains.append([name, time, idx, line])
 
for i in range(N-1):
    best = i
    for j in range(i+1, N):
        if trains[j][0] < trains[best][0]:
            best = j
        elif trains[j][0] == trains[best][0]:
            if trains[j][1] > trains[best][1]:
                best = j
            elif trains[j][1] == trains[best][1]:
                if trains[j][2] < trains[best][2]:
                    best = j
    if best != i:
        trains[i], trains[best] = trains[best], trains[i]
 
for t in trains:
    print(t[3])