import sys
input=sys.stdin.readline
from itertools import combinations_with_replacement as cwr

n,m = map(int,input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)
data = list(cwr(arr,m),)
for i in data:
    print(*i)