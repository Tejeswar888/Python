#encapsulation
#publicdata()
'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
a=child()
a.method1()
a.method2()'''



#_protecteddata()
'''class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
a=child()
a.method1()
a.method2()
print(a._protecteddata)'''


#__privatedata()
'''class parent():
    __privatedata="pavani"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
a=child()
a.method1()
a.method2()'''


#abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method()'''

'''class A():
    def method1(self):
        print("codegnan")
obj1=A()
obj1.method1()'''

#using abstract
'''from abc import ABC,abstractmethod
class A():
    def method1(self):
        print("python full stack")
obj1=A()
obj1.method1()'''

#abstract method
'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("python full stack")
obj1=A()
obj1.method1()'''#error


'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("python")
    @abstractmethod
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("java")
    def method3(self):
        print("dsa")
obj1=B()
obj1.method1()
obj1.method2()
obj1.method3()'''
    

