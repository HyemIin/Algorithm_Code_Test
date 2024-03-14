import sys
input = sys.stdin.readline
INF = int(1e9)

def search(start):
    distance[start] = 0
    for i in range(1,n+1):
        for j in range(m):
            now,next,cost = edge[j][0],edge[j][1],edge[j][2]
            if distance[now] != INF and distance[next] > distance[now] + cost:
                distance[next] = distance[now] + cost
                if i == n:
                    return True
    return False


n,m = map(int,input().split())
edge = [list(map(int,input().split())) for _ in range(m)]
distance = [INF]*(n+1)

if search(1):
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])