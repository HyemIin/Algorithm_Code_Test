import sys
input=sys.stdin.readline
from itertools import product

n,k = map(int,input().split())

data = [1,2,3]
result = []
for i in range(1,n+1):
    combi = list(product(data,repeat=i))
    for j in range(len(combi)):
        if sum(combi[j]) == n:
            result.append(combi[j])

result = sorted(result)

if k <= len(result):
    print(*result[k-1],sep="+")
else:
    print(-1)