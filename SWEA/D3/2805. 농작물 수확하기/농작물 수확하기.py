t = int(input())
for k in range(t):
    size = int(input())
    graph = [list(map(int, input())) for _ in range(size)]
    count = 0
    lst = []
    #상단
    for i in range(size//2):
        for j in range(size//2-i,size//2+i+1):
            count += graph[i][j]
    lst.append(count)
    #중단
    lst.append(sum(graph[size//2]))
    #하단
    count = 0
    for i in range(1,size//2+1):
        for j in range(i,size-i):
            count += graph[size//2+i][j]
    lst.append(count)
    print('#'+f"{k+1}",sum(lst))