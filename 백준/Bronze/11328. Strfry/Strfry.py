n = int(input())
for i in range(n):
    string1,string2 = map(str,input().split())
    ans1 = sorted(string1)
    ans2 = sorted(string2)
    if ans1 == ans2:
        print("Possible")
    else:
        print("Impossible")