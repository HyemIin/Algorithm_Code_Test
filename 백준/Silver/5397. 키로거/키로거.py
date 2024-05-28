from collections import deque
for _ in range(int(input())):
    string = list(input())
    s1 = []
    s2 = deque()
    for i in string:
        if i =="<":
            if s1:
              s2.insert(0,s1.pop())
        elif i == ">":
            if s2:
                s1.append(s2.popleft())
        elif i == "-":
            if s1:
                s1.pop()
        else:
            s1.append(i)
    s1 = s1 + list(s2)
    print("".join(s1))