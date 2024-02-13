import sys
input=sys.stdin.readline
t = int(input())
for tc in range(t):
    n = int(input())
    dp=[0,1,2,4,7,13]
    for i in range(6,n+1):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[n])