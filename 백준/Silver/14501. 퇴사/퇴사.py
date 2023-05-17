def dfs(sdate,sprice):
    global max_price
    if sdate == n:
        max_price=max(sprice,max_price)
        return
    dfs(sdate+1,sprice)
    if sdate+data[sdate][0] <= n:
        dfs(sdate+data[sdate][0],sprice+data[sdate][1])


n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
max_price = 0
dfs(0,0)
print(max_price)