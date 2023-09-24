s = input()
stack = []
# <,>가 없는 경우
if "<" not in s:
    for i in range(len(s)):
        if s[i] !=" ":
            stack.append(s[i])
        if s[i] == " " or i == (len(s)-1):
            stack.reverse()
            print("".join(stack), end=" ")
            stack=[]

# <,>가 있는 경우
else:
    for i in range(len(s)):
        stack.append(s[i])
        if s[i] == ">":
            print("".join(stack),end="")
            stack=[]
            continue
        if s[i] ==" " and "<" not in stack:
            stack.reverse()
            stack=stack[1:]
            print("".join(stack), end=" ")
            stack = []
            continue
        if s[i] =="<" and len(stack) != 1:
            stack.reverse()
            stack = stack[1:]
            print("".join(stack), end="")
            stack = ["<"]
        if i == len(s)-1 and len(stack) != 0:
            stack.reverse()
            print("".join(stack), end="")