import sys
input = sys.stdin.readline

n,c = map(int,input().split())
data = []
for i in range(n):
    data.append(int(input()))
data= sorted(data)

start = 1
end = data[-1]-data[0]
answer = 0

while start <= end:
    mid = (start+end)//2
    count,current = 1,data[0]

    for i in range(len(data)):
        if data[i] - current >= mid:
            count += 1
            current = data[i]
    if count >= c:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)