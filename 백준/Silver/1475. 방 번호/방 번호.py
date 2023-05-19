import math
n = (input())
data = [0]*(10)
for i in n:
    data[int(i)] += 1
if data.index(max(data)) != 6 and data.index(max(data)) != 9:
    print(max(data))
else:
    if data[7] != max(data) and data[8] != max(data):
        print(math.ceil((data[6]+data[9])/2))
    else:
        print(max(data))