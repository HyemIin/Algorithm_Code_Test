n,m = map(int,input().split())
a = list(map(int,input().split()))
s,e,count =0,1,0

while e <= n and s <= e:
    sums = a[s:e]
    result = sum(sums)
    if result < m:
        e += 1
    elif result > m:
        s += 1
    else:
        count += 1
        e += 1

print(count)