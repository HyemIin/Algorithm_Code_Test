n = int(input())
graph = list(map(int,input().split()))
dp = [0]*(n+1)

for i in range(1,n):
    for j in range(i):
        if graph[i] > graph[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp)+1)