import sys
input=sys.stdin.readline
from itertools import combinations

while True:
    data = list(map(int,input().split()))
    if data == [0]:
        break
    else:
        k = data[0]
        data = sorted(data[1:])
        pr = list(combinations(data,6))

        for i in pr:
            print(*i)
    print()