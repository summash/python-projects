class employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'the name is {self.name} ')

class dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f'the dance is {self.dance}')

class danceremployee(dancer,employee,):#multiple
    def __init__(self,dance, name):
        self.dance=dance
        self.name=name
        
o=danceremployee('kathak', 'kartik')
print(o.name)
print(o.dance)
o.show()
print(danceremployee.mro())