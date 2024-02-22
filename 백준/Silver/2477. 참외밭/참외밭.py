k = int(input())
graph = [list(map(int,input().split())) for _ in range(6)]
length = 0
height = 0
for i in range(6):
    if graph[i][0] == 1 or graph[i][0] == 2:
        length = max(length,graph[i][1])
    else:
        height = max(height,graph[i][1])
squaresize = length*height
wide = []
for i in range(6):
    if graph[i][1] == length:
        wide.append(i)
    elif graph[i][1] == height:
        wide.append(i)


mini1 = abs(graph[(wide[0]-1)%6][1]-graph[(wide[0]+1)%6][1])
mini2 = abs(graph[(wide[1]-1)%6][1]-graph[(wide[1]+1)%6][1])
minisize = mini1 * mini2

print((squaresize-minisize)*k)