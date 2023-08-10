import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

big = 0
def dfs(x,y):
    global big
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if graph[x][y] == 0:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        big += 1
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)

n,m,k = map(int,input().split())
trash = [list(map(int,input().split())) for _ in range(k)]
graph = [[0]*m for _ in range(n)]
for i in trash:
    graph[i[0]-1][i[1]-1] = 1


result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dfs(i,j)
            result.append(big)
            big = 0
print(max(result))
