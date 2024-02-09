import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    wear = []
    data = [list(map(str,input().split())) for _ in range(n)]
    if len(data) == 0:
        print(0)
    else:
        for j in range(len(data)):
            wear.append(data[j][1])
        count = [1]
        wear = sorted(wear)

        for j in range(1,len(wear)):
            if wear[j] != wear[j-1]:
                count.append(1)
            else:
                count[-1] += 1


        cnt = 1
        for j in range(len(count)):
            cnt *= (count[j]+1)
        print(cnt-1)