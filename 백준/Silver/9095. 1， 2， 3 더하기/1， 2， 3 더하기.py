import sys
from itertools import product
input = sys.stdin.readline

data = [1,2,3]
t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in range(1,n+1):
        hap = product(data,repeat = j)
        for k in hap:
            if sum(k) == n:
                count += 1
    print(count)