for i in range(10):
    t = int(input())
    graph = [list(map(str, input())) for _ in range(8)]
    lst = []
    for k in graph:
        for j in range(9-t):
            count = 0
            for q in range(t//2):
                if k[j+q] == k[j+t-q-1]:
                    count +=1
                if count == t//2:
                    lst.append(1)

    for k in range(8):
        for j in range(9-t):
            cnt = 0
            for q in range(t//2):
                if graph[j+q][k] == graph[j+t-q-1][k]:
                    cnt += 1
                if cnt == t//2:
                    lst.append(1)

    print('#'+f"{i+1}",len(lst))