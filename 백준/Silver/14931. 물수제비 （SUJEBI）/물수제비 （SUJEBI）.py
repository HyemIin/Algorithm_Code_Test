import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

def dfs(d,value):
    if d == l+1:
        return
    svalue = 0
    for i in range(1,l//d+1):
        svalue += data[d*i-1]
    if svalue > value:
        value = svalue
    if value > 0:
        point.append(value)
    else:
        point.append(0)
    dfs(d+1,value)

l = int(input())
data = list(map(int,input().split()))
point = [0]
dfs(1,0)
print(point.index(max(point)),max(point))