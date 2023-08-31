import sys
input = sys.stdin.readline

m,n = map(int,input().split())
data = list(map(int,input().split()))
start = 1
end = max(data)
answer = 0
while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(n):
        if data[i] >= mid:
            count += (data[i]//mid)
    if count >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)