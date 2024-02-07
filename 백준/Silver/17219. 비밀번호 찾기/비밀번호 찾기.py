import sys
input = sys.stdin.readline

n,m = map(int,input().split())
site_name = dict(input().split() for _ in range(n))

for i in range(m):
    site = input().rstrip()
    if site in site_name:
        print(site_name[site])
