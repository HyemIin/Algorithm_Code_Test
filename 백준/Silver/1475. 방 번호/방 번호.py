seet = [0,0,0,0,0,0,0,0,0,0]
count = 1
n = input()
for x in n:
    i = int(x)
    if i == 6 or i == 9:
         if seet[6] - seet[9] < 0:
             seet[6] += 1
         else:
             seet[9] += 1
    else:
        seet[i] += 1

print(max(seet))