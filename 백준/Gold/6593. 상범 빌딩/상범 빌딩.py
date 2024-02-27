from collections import deque

dz = [1,-1,0,0,0,0]
dx = [0,0,1,-1,0,0]
dy = [0,0,0,0,1,-1]

def bfs(i,j,k):
    queue.append((i,j,k))
    visited[i][j][k] = 1
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<r and 0<= ny<c and 0<=nz<l:
                if graph[nz][nx][ny] == "E":
                    print("Escaped in {0} minute(s).".format(visited[z][x][y]))
                    return
                if graph[nz][nx][ny] == "." and visited[nz][nx][ny] == 0:
                    visited[nz][nx][ny] = visited[z][x][y] + 1
                    queue.append((nz,nx,ny))
    print("Trapped!")


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    visited = [[[0] * c for _ in range(r)] for _ in range(l)]
    queue = deque()
    graph = []
    for i in range(l):
        graph.append([list(map(str,input())) for _ in range(r)])
        blank = input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == "S":
                    bfs(i,j,k)
                    break