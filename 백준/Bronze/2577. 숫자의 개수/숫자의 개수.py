ans = 1
for _ in range(3):
    ans *= int(input())
answer = [0] * 10
for i in range(len(str(ans))):
    answer[int(str(ans)[i])] += 1
for i in answer:
    print(i)