from collections import deque

n,m = map(int, input().split())
graph = [ list(map(int,input())) for i in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or 0 > ny or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
    return graph

count = 0
for i in range(m):
    if graph[-1][i] == 0:
        count += 1

lst = []
for i in range(m):
    if graph[0][i] == 0:
        lst.append(i)

for i in lst:
    bfs(0,i)

num = 0
for i in range(m):
    if graph[-1][i] == 0:
        num += 1
if num == count:
    print("NO")
else:
    print("YES")