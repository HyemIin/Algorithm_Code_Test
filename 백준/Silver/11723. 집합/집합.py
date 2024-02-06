import sys
input = sys.stdin.readline
m = int(input())

s = []
for _ in range(m):
    i = list(map(str, input().split()))
    if i[0] == "check" and i[1] in s:
        print(1)
    elif i[0] == "check" and i[1] not in s:
        print(0)
    elif i[0] == "add" and i[1] not in s:
        s.append(i[1])
    elif i[0] == "remove" and i[1] in s:
        s.remove(i[1])
    elif i[0] == "toggle" and i[1] in s:
        s.remove(i[1])
    elif i[0] == "toggle" and i[1] not in s:
        s.append(i[1])
    elif i[0] == "all":
        s  = ["1",'2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    elif i[0] == "empty":
        s = []