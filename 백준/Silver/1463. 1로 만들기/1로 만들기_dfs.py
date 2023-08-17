import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
count = 100000
def dfs(n,cnt):
    global count
    if count <= cnt:
        return
    if n == 1:
        count = min(count,cnt)
        return
    if n%3 == 0:
        dfs(n//3,cnt+1)
    if n%2 == 0:
        dfs(n//2,cnt+1)
    dfs(n-1,cnt+1)
dfs(n,0)
print(count)
