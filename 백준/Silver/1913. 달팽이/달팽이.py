import sys
input = sys.stdin.readline

n = int(input())
target = int(input())

graph = [[0]*n for _ in range(n)]
graph[n//2][n//2] = 1

x,y = n//2,n//2
for i in range(1,n+1):
    if i == n:
        for _ in range(i-1):
            graph[x-1][y] = graph[x][y]+1
            x=x-1
    else:
        for _ in range(i):
            if i%2 !=0:
                graph[x-1][y] = graph[x][y]+1
                x = x-1
            else:
                graph[x+1][y] = graph[x][y] + 1
                x = x+1
        for _ in range(i):
            if i % 2 != 0:
                graph[x][y+1] = graph[x][y] +1
                y = y+1
            else:
                graph[x][y-1] = graph[x][y] +1
                y = y-1

for i in range(n):
    print(*graph[i])

for i in range(n):
    for j in range(n):
        if graph[i][j] == target:
            print(i+1,end=" ")
            print(j+1)
            break