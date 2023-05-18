n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
graph = sorted(data,reverse=-1)
count = 1
grade = 0
lst = []
for i in graph:
    for j in range(len(graph)):
        if i[0] < graph[j][0] and i[1] < graph[j][1]:
            count += 1
    lst.append(count)
    count = 1
result = []
for i in data:
    for j in range(len(graph)):
        if i == graph[j]:
            result.append(lst[j])
            break
print(*result)