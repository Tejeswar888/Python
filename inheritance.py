#single-inheritance
'''class RBI():
    cash=100000
    def available_cash(cls):
        print("available_cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new_cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''


#multiple inheritance
'''class father():
    def weight(self):
        print("60 kgs")
class mother():
    def height(self):
        print("5.0 inches")
class Kid(father,mother):
    def dob(self):
        print("just born....")
c=Kid()
c.weight()
c.height()
c.dob()'''

#multilevel inheritance
'''class GrandParent():
    def land(self):
        print("2 acres")
class Parent(GrandParent):
    def house(self):
        print("100sqft")
class Child(Parent):
    def car(self):
        print("Thar")
c=Child()
c.land()
c.house()
c.car()'''

#heirarichal inheritance
'''class Employee():#parent class
    def company(self):
        print("HCL")
class Trainer(Employee):#child-1
    def teaching(self):
        print("Trainer teaching python course")
class Student(Trainer):#child-2
    def learning(self):
        print("Students preparing for exam")
a=Trainer()
a.company()
a.teaching()
b=Student()
b.company()
b.learning()'''

#hybrid inheritance
'''class Person():
    def details(self):
        print("pavani")
class Trainer(Person):
    def teach(self):
        print("trainer teachs python")
class Student(Person):
    def study(self):
        print("studies newspaper")
class program_manager(Student,Trainer):
    def management(self):
        print(" manages both trainer and student")
b=program_manager()
b.study()
b.teach()
b.details()
b.management()'''

#super()
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)
        print("child constructor")
a=child("pavani",19)
print(a.name)
print(a.age)'''