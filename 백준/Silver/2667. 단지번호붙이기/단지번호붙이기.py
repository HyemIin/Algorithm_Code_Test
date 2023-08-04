n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

count = 0
result = []
def dfs(x,y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    elif graph[x][y] == 0:
        return
    elif graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
    result.append(count)
    count = 0

final = []
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            pass
        else:
            dfs(i,j)
            cnt += 1
            final.append(sum(result))
            result = []
print(cnt)

final = sorted(final)
for i in range(cnt):
    print(final[i])