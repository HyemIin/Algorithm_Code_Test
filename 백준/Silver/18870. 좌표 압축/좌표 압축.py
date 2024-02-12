import sys
input=sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
sorted_data = sorted(list(set(data)))
dic_data = {sorted_data[i]:i for i in range(len(sorted_data))}

for i in data:
    print(dic_data[i],end=" ")