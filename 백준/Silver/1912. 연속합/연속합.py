n = int(input())
graph = list(map(int,input().split()))
for i in range(1,n):
    graph[i] = max(graph[i],graph[i-1]+graph[i])
print(max(graph))