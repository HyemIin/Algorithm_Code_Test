a = input()
list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = len(a)
for i in list:
    if i in a:
        count -= 1
        a = a.replace(i,'1')
print(len(a))