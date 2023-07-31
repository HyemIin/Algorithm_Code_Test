import sys
input=sys.stdin.readline
from itertools import product

n,m = map(int,input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)
data = list(product(arr,repeat=m),)
for i in data:
    print(*i)