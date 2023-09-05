import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data =list(map(int,input().split()))
start = 1
end = max(data)
answer = 0


while start <= end:
    total = 0
    for i in range(n):
        mid = (start+end)//2
        if data[i] >= mid:
            total += (data[i]-mid)
    if total < m:
        end = mid-1

    else:
        start = mid+1
        answer = mid


print(answer)