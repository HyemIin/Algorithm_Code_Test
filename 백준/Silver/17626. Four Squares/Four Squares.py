import sys
import math
input = sys.stdin.readline
n = int(input())
dp = [0,1]

for i in range(2,n+1):
    count = n
    for j in range(1, int(math.sqrt(i))+1):
        count = min(count,dp[i-j**2])
    dp.append(count+1)
print(dp[n])