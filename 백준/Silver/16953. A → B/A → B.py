a,b = map(str,input().split())
data = [b]

while True:
    if int(a) == int(b):

        print(len(data))
        break
    if int(a) > int(b):
        print(-1)
        break
    if b[-1] == "1":
        b = b[:-1]
        data.append(b)
    elif int(b)%2 == 0:
        b = str(int(b)//2)
        data.append(b)
    else:
        print(-1)
        break