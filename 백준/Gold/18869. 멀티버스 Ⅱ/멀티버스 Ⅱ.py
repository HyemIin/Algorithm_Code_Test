import sys
input = sys.stdin.readline

m,n = map(int,input().split())
space = {}

for i in range(m):
    data = list(map(int,input().split()))
    universe = sorted(list(set(data)))

    dic = {universe[k]:k for k in range(len(universe))}

    key = str([dic[l] for l in data])

    space[key] = space.get(key,0) + 1
print(sum(map(lambda x:x*(x-1)//2,space.values())))