#map()->each object from a collection and
#forms a new collection
'''a=[2,4,6,7,8,10,12,14,16,20,25]
b=[1,3,5,7,9,10,13,15,17,21]
c=list(map(max,a,b))
print(c)
d=list(map(min,a,b))
print(d)'''

#run_time input formats
'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the data").split(",")
print(a+b)'''

''''a,b=[x for x in input("data").split(",")]
print(a+b) #list comprehension
print(a,b)

a,b=[x for x in input("data").split(",")]
print(a+b)'''

'''a,b=map(str,input("enter the values").split(","))
print(a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)

a,b=[int(x) for x in input("enter the values")
      .split(",")]
print(a+b)'''

'''a,b=int(input("enter the values").split(","))
print(a+b) #error'''

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a=list(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a=tuple(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a=set(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a=input("enter the key and value pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''

'''while True:
    height = float(input("enter the height"))
    weight = float(input("enter the weight"))
    bmi = weight / (height) ** 2
    if bmi <= 18.5:
        print("under weight")
    elif bmi > 18.5 and bmi <= 24.5:
        print("healthy weight")
    elif bmi > 24.5 and bmi <= 29.5:
        print("over weight")
    elif bmi > 30:
        print("obesity")'''

'''def greetings(name):
    print("welcome",name)

a=3
b=8
print("the sum is",a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''details={"idnos":[10,20,30],
        "names":["sampath","vamsi","bhanu"],
        "marks":[60,70,90]}
import mymodule
mymodule.greetings("pooja")'''

#import mymodule

#import mymodule

'''import mymodule
a=mymodule.details["names"]
b=mymodule.details["idnos"]

print(a,b)
print(b)'''

'''if __name__ =="__main__":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''

def dummy():
    if  __name__ =="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()
