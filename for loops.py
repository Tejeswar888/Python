a=[10, 20 , 30, 40 , 50]
for i in a:
    print(i)

  
a=[10, 20 , 30, 40 , 50]
for i in a:
    print(i)
    print(type(a))
    print(type(i))


a={10, 20 , 30, 40 , 50}
for i in a:
    print(i)
print(type(a))
print(type(i))


a=(10, 20 , 30, 40 , 50)
for i in a:
    print(i, end = " ")
print('\n',type(a))


d = {'year':2026, 'month':'july', 'date':9}
for i in d:
    print(i)
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for i in d.items():
    print(i)
    print(type(d))
    print(type(i))

a = 'codegnan'
for i in a:
    print(i)

a = [3, 9.368, 'rainy', True, 5+6j]
for i in a:
    print(i)
    print(type(i))

fruits = ['apple', 'banana', 'mango']
a=[]
for i in fruits:
    a.append(i.upper())
print(a)


a=[10, 20 , 30 , 40, 50, 'code']
b=[]
for i in a:
    b.append(i)
    if type(i)==str:
        for j in i:
            b.append(j)
print(b)



#tasks
a=[10, 20 , 30 , 40, 50, 'code']
a.extend(a[-1])
print(a)

a=[2,3,5,6,7]
a.insert(2, 4)
print(a)

b=(5,6,7,8,9,10)
c=list(b)
c.pop()
d=tuple(c)
print(d)

e=[7,9,2,0,1,4,9,3,20]
e.sort()
print(e)


