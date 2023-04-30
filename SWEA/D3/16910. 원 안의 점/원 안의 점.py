t = int(input())
for i in range(t):
    n = int(input())
    # 0점 & 원의 꼭지점
    count = 0
    for j in range(n):
        for k in range(n):
            if k**2 + j**2 <= n**2:
                count += 1
    count = ((count-((2*n)))*4)+(4*n)+5
    print("#"+f"{i+1}",count)