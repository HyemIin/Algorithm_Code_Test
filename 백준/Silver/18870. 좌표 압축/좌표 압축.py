import sys
input=sys.stdin.readline
n = int(input())
data = list(map(int, input().split())) #좌표

sorted_data = sorted(list(set(data))) #배열로 받은 좌표 -> 오름차순 정렬 & set 자료구조를 활용하여 중복 제거 & 다시 리스트로 변경(편의상)
dic_data = {sorted_data[i]:i for i in range(len(sorted_data))} # 위에서 정렬한 리스트를 딕셔너리로 변경
for i in data: #좌표 for 문 돌려서 딕셔너리의 value값 출력
    print(dic_data[i],end=" ")