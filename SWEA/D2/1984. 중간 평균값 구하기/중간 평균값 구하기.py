t = int(input())
for i in range(1,t+1):
    number = list(map(int,input().split()))
    pick = []
    for k in number:
        if int(k) == max(number) or int(k) == min(number):
            pass
        else:
            pick.append(int(k))
    hap = sum(pick)
    average = hap/len(pick)
    print('#'+f"{i}",round(average))