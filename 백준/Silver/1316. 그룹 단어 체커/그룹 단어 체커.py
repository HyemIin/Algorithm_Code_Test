n = int(input())
count = 0
dup = []
for i in range(n):
    word = input()

    for j in range(len(word)):
        if j<2:
            pass
        else:
            if (word[j] in word[:j-1]) and word[j] != word[j-1]:
                dup.append(1)
                break
print(n-len(dup))