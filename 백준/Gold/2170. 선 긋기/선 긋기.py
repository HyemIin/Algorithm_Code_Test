import sys
input = sys.stdin.readline
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
data.sort()
left,right = data[0][0],data[0][1]
ans = 0
for i in range(1,n):
    if right >= data[i][1]:
        continue
    elif right < data[i][0]:
        ans += right - left
        left = data[i][0]
        right = data[i][1]
    else:
        right = data[i][1]
ans += right-left
print(ans)