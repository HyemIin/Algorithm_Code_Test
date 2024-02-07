import sys
input = sys.stdin.readline

n,m = map(int,input().split())
site_name = dict()

for i in range(n):
    name,pw = map(str,input().split())
    site_name[name] = pw

for i in range(m):
    site = input().rstrip()
    if site in site_name:
        print(site_name[site])