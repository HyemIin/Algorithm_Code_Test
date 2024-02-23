n = int(input())
data = [int(input()) for _ in range(n)]
minus = []
zero = []
one = []
plus = []

for i in range(len(data)):
    if data[i] < 0:
        minus.append(data[i])
    elif data[i] == 0:
        zero.append(0)
    elif data[i] == 1:
        one.append(1)
    else:
        plus.append(data[i])

minus = sorted(minus)
plus = sorted(plus, reverse=True)
#1 처리
answer = len(one)
# 양수 처리
if len(plus) >=2:
    if len(plus)%2 == 0:
        for i in range(0,len(plus),2):
            answer += plus[i]*plus[i+1]
    else:
        for i in range(0,len(plus)-1,2):
            answer += plus[i] * plus[i+1]
        answer += plus[-1]
elif len(plus) == 1:
    answer += plus[0]
#음수,0처리
if len(minus) >=2 :
    if len(minus)%2 == 0:
        for i in range(0, len(minus), 2):
            answer += minus[i] * minus[i+1]
    else:
        for i in range(0, len(minus)-1, 2):
            answer += minus[i] * minus[i+1]
        if len(zero) != 0:
            zero.remove(0)
            pass
        else:
            answer += minus[-1]
elif len(minus) == 1:
    if len(zero) != 0:
        zero.remove(0)
        pass
    else:
        answer += minus[0]

print(answer)