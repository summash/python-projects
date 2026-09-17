#access modifiers 
class employee:
    def __init__(self):
        self.name = 'harry'
        self.__gender = 'male'#private access modifier # called name mangling
        self._age= 21#protected access modifier 
a= employee()
a.emp1 = 5

print(a.name)
print(a._employee__gender)#private access modifiers can be acess indirectly
print(a.__dir__()) 
print(a._age)

