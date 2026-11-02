#Project using dictionary
d={}
n=int(input('enter how many members'))
for i in range(n):
    m=input('name')
    p=int(input('phone no'))
    d[m]=p
c=int(input('menu'))
if c==1:
    n=input('name')
    p=int(input('phone no'))
    d[n]=p
    print(d)
elif c==2:
    n=input('name')
    d.pop(n)
    print(d)
elif c==3:
    n=input('name')
    if n in d:
        print('yes present')
    else:
        print('not there')
elif c==4:
    for i,j in d.items():
        print(i , j)
