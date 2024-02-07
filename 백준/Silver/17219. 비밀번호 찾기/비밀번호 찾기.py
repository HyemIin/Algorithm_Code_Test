import sys
input = sys.stdin.readline #입출력

n,m = map(int,input().split()) # , N,M 값 받기
site_name = dict(input().split() for _ in range(n)) # HashTable의 일종인 dictionary를 활용하여  사이트/비밀번호 담기

for i in range(m):
    site = input().rstrip() # 찾고자하는 사이트 입력 받기
    print(site_name[site])