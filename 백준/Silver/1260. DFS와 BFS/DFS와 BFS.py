import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    print(v,end=" ")
    for i in map[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        num = queue.popleft()
        print(num,end=" ")
        for i in map[num]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True



n,m,v = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]

map = [[] for _ in range(n+1)]
for i in range(len(graph)):
    map[graph[i][0]].append(graph[i][1])
    map[graph[i][1]].append(graph[i][0])

for i in range(len(map)):
    map[i] = sorted(map[i])

visited = [False]*(n+1)
visited_bfs = [False for _ in range(n+1)]


dfs(v)
print()
bfs(v)