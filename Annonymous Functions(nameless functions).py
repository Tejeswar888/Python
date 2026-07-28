#annomy,ous functions(nameless functions)

#write a function to calculate 2*x+5 where x=5

'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input())
    print(2*x+5)
f()'''

#syntax
#a=lambda arg :expr
'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input())
b=lambda x:2*x+5
print(b(a))'''

#Take 2 Arguments and multipy it

'''a=lambda x,y:x*y
print(a(3,4))'''

'''a=int(input())
b=int(input())
c=lambda a,b:a*b
print(c(a,b))'''

#a="codegnan"
#CODEGNAN
'''a=lambda a:a.upper()
print(a("codegnan"))

#b="python course"
#Python Course
b="python course"
c=lamdba a:a.title()
print(c(b))'''

#First Name + Last Name = FullName
'''fname=input("first name")
lname=input("last name")
fullname=lambda fname, lname:(fname+" "+lname).title()
print(fullname(fname,lname))'''

'''fname,lname=[x for x in input ("enter the names").split(",")]
fullname=lambda fname,lname: (fname+" "+lname).title()
print(fullname(fname,lname))'''

#Filter()
a=[10,20,23,25,67,45,80,90,97,85,100]
#print all even numbers
'''if a%2==0:    #Error
    print(a)'''

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda x:x%2==0,a))
print(b)

b=list(filter(lambda x:x%2!=0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))'''

'''b=()
print(type(b))'''

'''c={}
print(type(c))'''

'''d=set()
print(type(d))'''

a=[[],(),set(),{}," ",3,5.6,"Teja",4+9j,True,False]
b=list(filter(a,None))
print(b)


