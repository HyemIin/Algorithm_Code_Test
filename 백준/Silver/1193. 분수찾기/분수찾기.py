x = int(input())
line = 1
lst = []
for i in range(1,x+1):
    if x > line:
        x = x - i
        line += 1
        lst.append(x)
    else:
        break
if len(lst)%2 ==0:
    a = len(lst) + 2 - x
    b = x
    print(f"{a}"+'/'+f'{b}')
else:
    a = x
    b = len(lst) + 2 - x
    print(f"{a}"+'/'+f'{b}')