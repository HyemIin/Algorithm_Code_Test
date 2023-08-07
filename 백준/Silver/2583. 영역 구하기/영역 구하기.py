import sys
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError)
input = sys.stdin.readline

m,n,k = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(k)]

graph=[[0]*n for _ in range(m)]

# 그래프 채우기
for spot in data:
    for i in range(spot[1],spot[3]):
        for j in range(spot[0],spot[2]):
            graph[i][j] = 1

count = 0
result = []
def dfs(x,y):
    global  count
    if x < 0 or x >= m or y < 0 or y >= n:
        return
    if graph[x][y] == 1:
        return
    if graph[x][y] == 0:
        graph[x][y] = 1
        count += 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            dfs(i,j)
            cnt += 1
            result.append(count)
            count = 0
print(cnt)
result = sorted(result)
print(*result)