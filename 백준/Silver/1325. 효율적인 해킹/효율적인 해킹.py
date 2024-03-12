from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data=[[] for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    data[b].append(a)

def bfs(s):
    q = deque()
    q.append(s)
    count = 0

    visited = [0] * (n+1)
    visited[s] = 1

    while q:
        point = q.popleft()
        for i in data[point]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                count += 1
    return count

result = []
for s in range(1,len(data)):
    result.append(bfs(s))

for i in range(len(result)):
    if max(result) == result[i]:
        print(i+1,end=" ")