#create a tuple,,sum,average,max,min
'''t=[]
n=int(input('enter how many times'))
for i in range(n):
    r=int(input('enter the value to tuple'))
    t.append(r)
print(tuple(t))
s=sum(t)
c=len(t)
a=s/c
ma=max(t)
mi=min(t)
print(s,a,ma,mi)'''

#Check if an element exist in the tuple

'''t=[]
n=int(input('enter how many times'))
for i in range(n):
    r=int(input('enter the value to tuple'))
    t.append(r)
print(tuple(t))
e=int(input('enter number to check in the tuple'))
for i in t:
    if i!=e:
        continue
    else:
        print('ys')'''

#to create a tuple without making into list
'''t=()
n=int(input('no'))
for i in range(n):
    p=int(input('no'))
    t=t+(p,)
print(t)'''

#Covert a tuple into a list, add an element, convert back to tuple.
'''t=(1,2,4,5)
l=list(t)
e=int(input('enter the element which u want to add to the list'))
l.append(e)
t=tuple(l)
print(t)'''

#count the frequency of each elemt in a tuple
'''t=(1,2,3,2,3,11,4,3)
l=list(t)
for i in set(l): ###set removes the duplicate elements
    
    print('frequency of',i,'is',l.count(i))'''

#unpack a tuple into three variable
'''t=(2,3,4)
a,b,c=t
print(a,b,c)'''



