import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 섬 구분
def dfs(x,y):
    global count
    if x <0 or y < 0 or x >= n or y >= n:
        return
    if graph[x][y] == 0:
        return
    if graph[x][y] == 1:
        graph[x][y] = count
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)

# 최단 거리 찾기
def bfs(k):
    global ans
    check =[ [-1]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j]== k:
                q.append([i,j])
                check[i][j] = 0
    while q:
        x,y = q.popleft()
        for dx,dy in (0,-1),(0,1),(1,0),(-1,0),:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > 0 and graph[nx][ny] != k:
                ans = min(ans,check[x][y])
                return
            if graph[nx][ny] == 0 and check[nx][ny] == -1:
                check[nx][ny] = check[x][y]+1
                q.append((nx,ny))


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
count = 2
ans = sys.maxsize
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            count += 1

for i in range(2,count):
    bfs(i)
print(ans)