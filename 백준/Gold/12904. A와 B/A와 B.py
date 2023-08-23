s = input()
t = input()
result = []
for i in range(len(t)):
    if t[-1] == 'A':
        t=t[0:len(t)-1]
    else:
        t=t[0:len(t)-1]
        t = t[::-1]
    if t == s:
        print(1)
        result.append(1)
        break

if len(result) == 0:
    print(0)