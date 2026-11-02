#LIST
#1.WAP to find the largest and smallest element in a list without using built-in function
'''l=[12,456,4,3,6,67]
max=0
min=l[0]
for i in l:
    if i>max:
        max=i
    elif i<min:
        min=i
print(max)
print(min)'''

#2.Remove duplicate element from the list
'''l=list(input('list'))
o=[]
for i in l:
    if i not in o:
        o.append(i)
print(o)'''

#OOORR

'''l=[12,4,5,7,12]    
for i in l:
    if l.count(i)>1:
        l.remove(i)
        
print(l)'''






#3.WAP to reverse a list without using reverse() or slicing.
'''l=[1,2,3,4]
p=[]
for i in range(len(l)-1,-1,-1):
    p.append(l[i])
print(p)'''

#4.Find the second largest number in a list.
'''l=[1,2,3,4]
l.sort()
print(l[-2])'''
    

#5.Merge two lists and sort the merged list.
'''l=[1,43,2,4,2]
l1=[4,5,3,6,25]
p=l+l1
p.sort()
print(p)'''

#6.count even and odd no. in a list.
'''l=[3,5,67,7,8,2,24]
e=0
o=0
for i in l:
    if i%2==0:
        e+=1
    else:
        o+=1
print("even count",e)
print("odd count",o)'''

 #7. Rotate a list by k position ( e.g, k=2 )
'''l=[1,2,3,45,6]
k=2
print(l[k:]+l[:k])'''


