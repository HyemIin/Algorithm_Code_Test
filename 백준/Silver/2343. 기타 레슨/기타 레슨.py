import sys
input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

answer = 0
start = max(data)
end = sum(data)

while start<=end:
    mid = (start+end)//2
    count,blue_sum=1,0
    for i in range(n):
        if blue_sum+data[i] > mid:
            count += 1
            blue_sum = 0
        blue_sum += data[i]

    if  count > m:
        start = mid +1
    else:
        end = mid -1
        answer = mid
print(answer)