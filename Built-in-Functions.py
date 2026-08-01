#Built-in-Functions

'''print(dir())

print(dir("__builtins__"))'''

'''a = "codegnan"
print(a)

print(list(a))
print(tuple(a))
print(set(a))'''
#print(dict(a))

#fromkeys()
'''b = dict.fromkeys(a)
print(b)

c = dict.fromkeys(a, "Tejs")
print(c)

c["d"]="hen"
print(c)'''

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=input("a value")
    b=input("b value")
    print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip()->we can combine multiple collections into
#one collection
'''a=[10,20,30,40,50]
names=["teja","dinesh","vamsi","sankalp","surya"]
print(a+names)

b=zip(a,names)
print(b)

c=list(zip(a,names))
print(c)

c=tuple(zip(a,names))
print(c)

c=set(zip(a,names))
print(c)

c=dict(zip(a,names))
print(c)'''

#enumerate() #we can give counter to the collection

'''names=["mythri","darshini","sarvani","srivarna","tejas"]
for i in range(len(names)):
    print(i,names[i])
    
b=dict(enumerate(names))
print(b)

b=dict(enumerate(names,100))
print(b)'''

#ASCII
#chr(),ord()
'''print(chr(65))

print(chr(90))

#print(chr("a"))

print(chr(91))

#ord()
print(ord("a"))

print(ord("z"))'''

#print(ord(56))

#print A to Z

#print a to z

'''for i in range(65,91):
    print(chr(i),end=" ")

for i in range(97,123):
    print(chr(i),end=" ")'''

'''a=input("enter the name")
for i in a:
    print(i,"-",ord(i))'''

#max(),min(),sum()
'''print(max(2,5,8,9,10,20,30))

print(min(2,4,6,8,10,12))

#print(sum(3,4))

a=2,3,4,5,6,7,8,9
print(sum(a))'''
