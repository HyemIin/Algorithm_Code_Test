t = int(input())
for i in range(t):
    bit = input()
    count = 0
    for k in range(1,len(bit)):
        if bit[k-1] != bit[k]:
            count += 1
    if bit[0] == '0':
        print('#'+f"{i+1}",count)
    else:
        print('#'+f"{i+1}",count+1)