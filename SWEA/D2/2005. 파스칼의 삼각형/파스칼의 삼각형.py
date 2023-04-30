t = int(input())
for i in range(t):
    size = int(input())
    triangle = [[0]*size for j in range(size)]
    # 맨 처음과 마지막은 모두 1
    for k in range(size):
        triangle[k][0] = 1
        triangle[k][k] = 1
    for k in range(2,size):
         for u in range(1,len(triangle[k])):
                 triangle[k][u] = triangle[k-1][u-1] + triangle[k-1][u]

    print('#'f'{i+1}')
    for k in range(len(triangle)):
        for q in triangle[k]:
            if q != 0:
                print(q,end=' ')
        print()
            
