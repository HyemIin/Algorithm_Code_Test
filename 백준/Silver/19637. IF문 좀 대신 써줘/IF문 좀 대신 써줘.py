import sys
from bisect import bisect_left

input = sys.stdin.readline
n, m = map(int, input().split())
title = []
power = [-1]
for i in range(n):
    t,p = map(str, input().split())
    title.append(t)
    power.append(int(p))

for i in range(m):
    p = int(input())
    index = bisect_left(power, p)
    print(title[index - 1])