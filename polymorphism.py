#polymorphism
#operator overloading
'''a=2; b=4
print(a+b)
print(a.__add__(b))
print(a.__sub__(b))
print(a.__mul__(b))
#print(a.__div__(b))
print(a.__pow__(2))
print(a.__eq__(2))
print(a.__le__(5))
print(a.__ge__(10))
print(a.__ge__(1))
a=[2,3,4,5,6];b=[6,7,8,9,10]#merging in list
print(a.__add__(b))
print(a.__getitem__(3))#accessing
print(b.__getitem__(4))
a="code";b="gnan"#concatenate
print(a.__add__(""+b))
a="python";b="course"
print(a.__add__(" "+b))
print("pavani".__add__(" "+"m").title())'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(4)
y=B(5)
#x=4
#y=5
print(x+y)'''


#method overloading
'''class new():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is:",a+b+c)
        elif a!=None and b!=None:
            print("the product is:",a*b)
        else:
            print("program ends.....")
x=new()
x.sum()
x.sum(2,4,7)
x.sum(4,5)'''


'''class new():
    def sum(self,a=1,b=2,c=3):
        if a!=1 and b!=12 and c!=3:
            print("the sum is:",a+b+c)
        elif a==1 and b!=6:
            print("the product is:",a*b)
        else:
            print("program ends.....")
x=new()
x.sum()'''


#method overriding
'''class Animal():
    def speak(self):
        print("animals can make sounds")
class Dog():
    def speak(self):
        print("dog can bark")
a=Animal()
b=Dog()
a.speak()
b.speak()'''


'''class Car():
    def vehicle(self):
        print("BMW")
class Bikes():
    def vehicle(self):
        print("R15")
a=Car()
b=Bikes()
a.vehicle()
b.vehicle()'''