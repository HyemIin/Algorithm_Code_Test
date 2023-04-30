X = int(input())
N = int(input())
list = []
for i in range(N):
    a,b = map(int,input().split())
    list.append(a*b)
if sum(list) == X:
    print('Yes')
else:
    print('No')