# quadratic equation
'''a=int(input('enter a'))
b=int(input('enter b'))
c=int(input('enter c'))
import math
d=b*b-4*a*c
if d==0:
        r=-b/2*a
        print(r)
elif d>0:
        r1=-b+math.sqrt(d)/2*a
        r2=-b-math.sqrt(d)/2*a
        print(r1)
        print(r2)
else:
        print('no real root exists')'''
#
n=int(input('enter a no'))
e=str(n)
l=len(e)
s=0
for i in range(l):
        s=s+n[i]
print(s)
