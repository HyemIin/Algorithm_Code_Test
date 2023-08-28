import sys
from bisect import bisect_left
input = sys.stdin.readline
n,m = map(int,input().split())
title = []
power = [-1]
for i in range(n):
    a = input().split()
    title.append(a[0])
    power.append(int(a[1]))

check = []
for i in range(m):
    check.append(int(input()))

for i in range(m):
    index = bisect_left(power,check[i])
    print(title[index-1])