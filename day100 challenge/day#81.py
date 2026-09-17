#multiple inheritence
class SuperClass1:
    num1 = 3

class SuperClass2:
    num2 = 5

class SubClass( SuperClass1, SuperClass2):
    def addition(self):
        return self.num1 + self.num2

obj = SubClass()
print(obj.addition())

#hierarchical inheritence
class SuperClass:
    x = 3
class SubClass1(SuperClass):
    pass
class SubClass2(SuperClass):
    pass
class SubClass3(SuperClass):
    pass
a = SubClass1()
b = SubClass2()
c = SubClass3()
print(a.x, b.x, c.x)