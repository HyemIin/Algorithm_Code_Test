import sys
input=sys.stdin.readline
n = int(input())
winner = 1 #홀수면 SK, 짝수면 CY
ans = n
while 1:
    if ans%3 == 0:
        answer = ans // 3
        if answer%2 != 0:
            if winner%2 != 0:
                print("SK")
                break
            else:
                print("CY")
                break
        else:
            if winner%2 != 0:
                print("CY")
                break
            else:
                print("SK")
                break
    else:
        ans -= 1
        winner += 1