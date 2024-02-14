import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if data[i][j] == "I":
            x,y = i,j

dx = [1,-1,0,0]
dy = [0,0,1,-1]
count = 0
q = deque()
q.append([x,y])

while q:
    x,y = q.popleft()
    for v in range(4):
        ux,uy = x+ dx[v], y+dy[v]
        if ux < 0 or uy < 0 or ux >= n or uy >= m or data[ux][uy] == "X":
            continue
        if data[ux][uy] == "I" or data[ux][uy] == "O":
            data[ux][uy] = "X"
            q.append([ux,uy])
            continue
        if data[ux][uy] == "P":
            data[ux][uy] = "X"
            count += 1
            q.append([ux, uy])
            continue
if count != 0:
    print(count)
else:
    print("TT")