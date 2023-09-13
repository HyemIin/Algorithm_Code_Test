import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

direct = [(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y):
    if dp[x][y] == -1:
        dp[x][y] = 0

        for ux,uy in direct:
            dx = x+ux
            dy = y + uy
            if n>dx>=0 and n>dy>=0 and graph[dx][dy] > graph[x][y]:
                dp[x][y] = max(dp[x][y],dfs(dx,dy))
    return dp[x][y] + 1


count = 0
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        count = max(dfs(i,j),count)

print(count)