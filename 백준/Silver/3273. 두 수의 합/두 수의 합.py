n = int(input())
data = list(map(int,input().split()))
data.sort()
x = int(input())
left,right = 0,n-1
ans = 0
while left < right:
    tmp = data[left] + data[right]
    if tmp == x:
        ans += 1
        left += 1
    elif tmp < x:
        left += 1
    elif tmp > x:
        right -= 1
print(ans)