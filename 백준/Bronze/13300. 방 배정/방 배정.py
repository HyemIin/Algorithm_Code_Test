import math
n,k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
room = []
for _ in range(7):
    room.append([0,0])
for child in data:
    room[child[1]][child[0]] += 1
count = 0
for i in range(1,7):
    for j in range(2):
        if room[i][j] == 0:
            continue
        elif 0 < room[i][j] <= k:
            count += 1
        elif room[i][j] > k:
            count += math.ceil(room[i][j]/k)
print(count)