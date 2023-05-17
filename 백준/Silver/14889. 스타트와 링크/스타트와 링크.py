from itertools import combinations
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
#조합 만들기
lst = []
for i in range(1,n+1):
    lst.append(i)
data = list(combinations(lst,n//2))
dp = []
hip = 0
hop = 0
#com = 2개쌍으로 만든 조합
for i in range(len(data)):
    com = list(combinations(data[i],2))
    for a,b in com:
        hip += (graph[a-1][b-1]+graph[b-1][a-1])
    rev = []
    for k in range(1,n+1):
        if k not in data[i]:
            rev.append(k)
    com_rev = list(combinations(rev,2))
    for a,b in com_rev:
        hop += (graph[a-1][b-1]+graph[b-1][a-1])
    dp.append(hip-hop)
    hip=0
    hop = 0
for i in range(len(dp)):
    if dp[i]*(-1) >0:
        dp[i] = -1*dp[i]
print(min(dp))