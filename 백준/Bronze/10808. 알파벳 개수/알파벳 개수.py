s = sorted(input())
ans = [0] * 26
for i in s:
    ans[ord(i)-97] += 1
print(*ans)