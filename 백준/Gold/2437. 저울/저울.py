import sys
input=sys.stdin.readline

n = int(input())
data = sorted(list(map(int,input().split())))

target = 1
for i in data:
    if target < i:
        break
    target += i

print(target)