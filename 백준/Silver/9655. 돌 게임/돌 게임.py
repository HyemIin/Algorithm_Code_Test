import sys
input=sys.stdin.readline
n = int(input())
sequence = 1 #홀수면 SK, 짝수면 CY
while 1:
    if n%3 == 0: # n이 3의 배수라면
        answer = n // 3
        if answer%2 != 0 and sequence%2 != 0: # answer가 짝수라면 +  지금 차례 사람이 SK라면
            print("SK")
            break
        elif answer%2 != 0 and sequence%2 == 0:
            print("CY")
            break
        elif answer%2 == 0 and sequence%2 != 0:
            print("CY")
            break
        elif answer%2 == 0 and sequence%2 == 0:
            print("SK")
            break
    else:
        n -= 1
        sequence += 1