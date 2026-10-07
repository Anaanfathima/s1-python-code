#Reverse the Number
n=int(input('enter a no'))
n1=0
s=str(n)
l=len(s)
for i in range(l):
    r=n%10
    n1=n1*10+r
    n=n//10
print(n1)
