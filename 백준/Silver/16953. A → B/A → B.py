n,m = map(str,input().split())
data=[m]
while True:
    if int(n) == int(m):
        print(len(data))
        break
    if int(n) > int(m):
        print(-1)
        break
    if m[-1] == "1":
        m = m[:-1]
        data.append(m)
    elif int(m)%2 == 0:
        m = str(int(m)//2)
        data.append(m)
    else:
        print(-1)
        break