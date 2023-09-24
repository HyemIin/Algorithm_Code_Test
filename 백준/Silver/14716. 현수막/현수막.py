import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return
    elif graph[x][y] == 0:
        return
    elif graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x-1,y-1)
        dfs(x+1,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y+1)

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]

count = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            count += 1
print(count)