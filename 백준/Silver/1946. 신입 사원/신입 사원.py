import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    data = sorted(data)
    min_value = data[0][1]
    count = 1
    for i in range(n):
        if data[i][1] < min_value:
            count += 1
            min_value = data[i][1]
    print(count)