import sys
from collections import deque
input=sys.stdin.readline

s1 = list(input().strip())
s2 = deque()

n = int(input())
data = [list(map(str,input().split())) for _ in range(n)]

for command in data:
    # L인 경우
    if command[0] == "L":
        if s1:
            s2.insert(0,s1.pop())
    # D인 경우
    elif command[0] =="D":
        if s2:
            s1.append(s2.popleft())
    # B인 경우
    elif command[0] == "B":
        if s1:
            s1.pop()
    else:
        s1.append(command[1])


s1.extend((s2))
print("".join(s1))