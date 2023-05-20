t = int(input())
for i in range(1,t+1):
    sentence = input()
    count = 1
    for k in range(len(sentence)):
        count += 1
        if sentence[:k+1] == sentence[k+1:len(sentence[:k+1])+k+1]:
            print('#'+f"{i}",k+1)
            break