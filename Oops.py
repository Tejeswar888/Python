#oops
#syntax
'''class Classname():
    #attributes
    name="pooja"
    age=28
    place="vja"
    def fname(method_name):
        print(statements........)
obj=Classname()
obj.fname()'''

#class declaration
'''class details():
    name="pooja"
    age=28
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''

#class declaration
'''class details():
    name="pooja"
    age=28
    place="vja"
    def display(self):
        print(self.name,self.age,self.place)
a=details()
print(dir(a))
a.display()'''


#object instantiation
'''class details:
    def data(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name, self.age, self.place)
a = details()
print(dir(a))
a.data("pooja", 28, "vja")
a.display()
b = details()
b.data("priya", 27, "vja")
b.display()'''

#object intialization
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("pooja",28,"vja")
print(dir(a))
a.display()'''

'''class Details():
    #creating a constructor
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def display(self):
        print(self.name, self.age, self.place)

a = Details(input("name"), int(input("age")), input("place"))
print(dir(a))
a.display()'''

'''class Details():
    #creating a constructor
    def __init__(self):
        self.name=input("name")
        self.age=int(input("age"))
        self.place=input("place")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

# diff b/w _ and __
'''class Employee():
    def __init__(self):
        self.name = "pooja"
        self._mailid = "pooja@codegnan.com"
        self.__salary = 30000 # private variable

a = Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary) # error
print(a._Employee__salary)'''

# diff b/w _ and __
'''class Employee1:

    def __init__(self):
        self.name = "pooja"
        self._mailid = "pooja@codegnan.com"
        self.__salary = 30000  # private variable


class Employee2:

    def __init__(self):
        self.name = "preethi"
        self._mailid = "preethi@codegnan.com"
        self.__salary = 40000  # private variable
a = Employee1()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary) #error
print(a._Employee1__salary)
b=Employee2()
print(dir(b))
print(b.name)
print(b._mailid)
#print(b.__salary) #error
print(b._Employee2__salary)'''