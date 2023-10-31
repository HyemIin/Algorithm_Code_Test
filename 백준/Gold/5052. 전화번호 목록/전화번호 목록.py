import sys
# input = sys.stdin.readline().rstrip

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    phone_number = []
    for j in range(n):
        phone_number.append(sys.stdin.readline().rstrip())

    phone_number.sort()

    answer = "YES"
    for j in range(n-1):
        long = len(phone_number[j])
        if phone_number[j+1][:long] == phone_number[j]:
            answer = "NO"
            break

    print(answer)