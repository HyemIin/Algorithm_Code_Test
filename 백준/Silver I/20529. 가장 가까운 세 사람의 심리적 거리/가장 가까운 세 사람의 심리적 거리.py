import sys
from itertools import combinations
input = sys.stdin.readline

def close_mind(x,y):
    count = 0
    x = list(x)
    y = list(y)
    for i in range(4):
        if x[i] != y[i]:
            count += 1
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = list(map(str,input().split())) ##정렬하고 3개 같은거 있는지 찾는게 빠를지
    if n > 32:
        print(0)
    else:
        mbti_combi = list(combinations(mbti,3))
        cnt = 100
        for x,y,z in mbti_combi:
            cnt = min(cnt,close_mind(x,y)+close_mind(x,z)+close_mind(y,z))
        print(cnt)