import sys
sys.setrecursionlimit(10**6) # 재귀 제한 늘이기

def dfs(x,y):
    global count
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if data[x][y] == "X":
        return
    if data[x][y] == "P":
        data[x][y] = "X"
        count += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    if data[x][y] == "O" or data[x][y] == "I":
        data[x][y] = "X"
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)

input=sys.stdin.readline
n,m = map(int,input().split())
data = [list(input().rstrip()) for _ in range(n)]
count = 0
x,y = 0,0
for i in range(n):
    for j in range(m):
        if data[i][j] == "I":
            x,y = i,j
dfs(x,y)

if count != 0:
    print(count)
else:
    print("TT")