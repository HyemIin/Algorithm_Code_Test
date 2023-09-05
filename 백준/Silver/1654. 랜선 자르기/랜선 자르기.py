import sys
input = sys.stdin.readline

k,n = map(int,input().split())
data =[]

for i in range(k):
    data.append(int(input()))
start = 1
end = max(data)
answer = 0

while start <= end:
    mid = (start+end)//2
    count = 0
    for i in range(k):
        if data[i] >= mid:
            count += data[i]//mid
    if count >= n:
        start = mid+1
        answer = mid
    else:
        end = mid -1



print(answer)