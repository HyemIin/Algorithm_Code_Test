import sys
input = sys.stdin.readline

# x 가로줄의 n이 있는지 확인
def checkRow(x, n):
    for i in range(9):
        if n == graph[x][i]:
            return False
    return True


# y 세로줄의 n이 있는지 확인
def checkCol(y, n):
    for i in range(9):
        if n == graph[i][y]:
            return False
    return True


# 3x3 크기의 사각형의 n이 있는지 확인
def checkRect(x, y, n):
    nx = (x // 3) * 3
    ny =( y // 3) * 3
    for i in range(3):
        for j in range(3):
            if n == graph[nx+i][ny+j]:
                return False
    return True


# dfs + 백트래킹
def solution(n):
    # 스도쿠의 빈 칸을 채웠다면
    if len(blank) == n:
        for i in range(9):
            print(*graph[i])
        exit(0)
    for i in range(1,10):
        x = blank[n][0]
        y = blank[n][1]
        if checkRow(x,i) and checkCol(y,i) and checkRect(x,y,i):
            graph[x][y] = i
            solution(n+1)
            graph[x][y] = 0


graph = []
blank = []
for i in range(9):
    graph.append(list(map(int, input().split())))
    for j in range(9):
        if graph[i][j] == 0:
            blank.append([i, j])


solution(0)