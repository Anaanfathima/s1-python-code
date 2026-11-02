#Create a dictionary of 5 students with name:mark, and find the student with highest markand lowest
'''d={}
n=int(input('how many times'))
for i in range(n):
    e=input('enter the name')
    m=int(input('enter the mark'))
    d[e]=m
print(d)
max=0
min=100
for i,j in d.items():
    if max<j:
        max=j
        s=i
    if min>j:
        min=j
        t=i
print(s,'Scored Highest Mark of',max)
print(t,'scored Lowest MArk of',min)'''

#merge two dictionaries into one
'''d={1:2,3:4}
d2={4:9,5:4}
d.update(d2)
print(d)'''

#count each character in a string using a dictionary
'''s=input('enter a string')
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        
print(d)'''
#sort a dictionary by kleys and by values
#by taking list
d={'a':2,'b':34,'c':32}
'''l=[]
o=[]
for i,j in d.items():
    l.append(i)
    o.append(j)
l.sort()
o.sort()
print(l)
print(o)'''
#keys and values
'''d2={}
for i in sorted(d):
    d2[i]=d[i]
print(d2,'sorted by keys')
d3={}
for i in sorted(d, key=d.get):
    d3[i]=d[i]
print(d3,'sorted by values')'''

#WAP to check whether two dic are equal
'''d={'a':2,'b':34,'c':32}
d1={'a':2,'b':34,'c':32}
if d==d1:
    print('equal')'''
    
#create a dictionary from two lists key list and value list( error if keys are5 and values are 4 , but it will work for 4 keys and 5 values ignore the last one)
'''lk=[1,2,4,5]
lv=[7,6,5,2]
d={}
for i in range(len(lk)):
    d[lk[i]]=lv[i]
print(d)

##OR(using zip function)
d=dict(zip(lk,lv))
print(d)'''

#Remove a key from dic if it exists,otherwise key not find error
'''d={1: 7, 2: 6, 4: 5, 5: 2}
n=int(input('enter the no to remove'))
if n in d:
    d.pop(n)
else:
    print('keynotfound')
print(d)'''


