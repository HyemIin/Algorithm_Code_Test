n = int(input())
# 시작, 끝, 카운트, 덧셈 결과 값 = 0 으로 초기화
s,e,count,result = 0,0,0,0

# end 값이 n 을 넘지 않을 때 까 반복
while e <= n:
    if result < n:
        e += 1
        result += e
    elif result > n:
        result -= s
        s += 1
    else:
        count += 1
        e += 1
        result += e
print(count)