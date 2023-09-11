import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x <0 or y<0 or x>=m or y>= n:
        return
    if graph[x][y] == 0:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)


t = int(input())
for i in range(1,t+1):
    count = 0
    m,n,k = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(k)]
    graph = []
    for q in range(m):
        graph.append([0]*n)
    for a,b in data:
        graph[a][b]=1

    for j in range(m):
        for k in range(n):
            if graph[j][k] == 1:
                dfs(j,k)
                count += 1
    print(count)