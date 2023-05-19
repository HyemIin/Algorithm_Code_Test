t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    data = input().split()
    target = data[m]
    sequence = 0
    while m != -1:
        if data[0] == max(data):
            sequence += 1
            data.pop(0)
            if m == 0:
                m = -1
            else:
                m -= 1
        else:
            data.append(data.pop(0))
            if m == 0:
                m = len(data)-1
            else:
                m -= 1
    print(sequence)