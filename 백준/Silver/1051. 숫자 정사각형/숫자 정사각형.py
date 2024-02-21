n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
lst = []
for i in range(min(n,m)):
    for k in range(n-i):
        for j in range(m-i):
            if graph[k][j] == graph[k][j+i] == graph[k+i][j] == graph[k+i][j+i]:
                lst.append(i+1)
print(max(lst)**2)