# Global and local variables
#first case of global variable
'''a=3
def check1():
    print("inside value is",a)
check1()
print("outside value is",a)'''

'''#second case of global variable
a=4
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''

'''#third case of both global and local variables
a=2
b=9
def check3() :
    a=7
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=14#local variable
    b=b+a
    print("value of b is",b)
check3()
print("a value is",a)
print("b value is",b)'''

'''#usage of global keyword
a=5
def final():
    global a,b
    print("inside value is",a)
    a=10
    print("updated value is",a)
    #global b
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

'''# attendance tracker
students = int(input("enter the students"))
p = 0
a = 0
for i in range(1, students + 1):
    attendance = input(f"student{i} (p/a)")
    if attendance == "p":
        p += 1
    elif attendance == "a":
        a += 1
print("..........attendance tracker..........")
print("total students", students)
print("total presenties", p)
print("total absenties", a)'''
