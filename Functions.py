#Functions
'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)'''

'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#**,%,//
'''def calculate(a,b):
    print("the int div is",a//b)
    print("the mod is",a%b)
    print("the pow is",a**b)
calculate(10,20)
calculate(2,4)
calculate(5,8)'''

'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def add():
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)
    add()
add()'''

'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(4,6)'''

'''def mul(a,b):
    return a*b
print(mul(7,3))'''

#print v/s return
'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,3)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(2,3))'''

#splitbill
'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    c=b//a
    print("per head bill is",b//a)
splitbill()'''

'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    print("per head bill is {}".format(b//a))
    print(f"perhead bill is {b//a}")
splitbill()'''

'''def splitbill():
    a=int(input("enter the total members"))
    b=int(input("enter the amount"))
    c=b//a
    print("per head bill is {}".format(c))
    print(f"perhead bill is {c}")
splitbill()'''

'''while True:
    def cal():
        a = int(input("a value"))
        b = int(input("b value"))
        option = int(input('''choose the option
        1.add
        2.sub
        3.mul'''))

        if option == 1:
            print(a + b)
        elif option == 2:
            print(a - b)
        elif option == 3:
            print(a * b)
    cal()'''




