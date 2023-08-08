import sys
from collections import deque
sys.setrecursionlimit(10**6) # 재귀의 깊이 변경 (RecursionError) # 전체 graph 크기가 1000을 넘어가면 재귀 깊이 변경해줄 것.(파이썬은 재귀 제한 1000번임)
input = sys.stdin.readline


dz = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]
def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and 0<= nz < h and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                queue.append([nz,nx,ny])

m,n,h = map(int,input().split())
graph = []
for i in range(h):
    graph.append([list(map(int,input().split())) for _ in range(n)])

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append([i,j,k])

bfs()
count = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                count += 1
                exit(0)

day = 0
if count == 0:
    for i in graph:
        for j in i:
            for k in j:
                if k > day:
                    day = k
    print(day-1)
