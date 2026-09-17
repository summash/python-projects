class parentclass:
    def parent_method(self):
        print('this is the parent method')
        
class childclass(parentclass):
    def parent_method(self):
        print('harry')
        super().parent_method()
    def child_method(self):
        print('this is the child method')
        
        super().parent_method()
        
child_object = childclass()
child_object.child_method()
child_object.parent_method()

class employee:
    def __init__(self,name,Id):
        self.name=name
        self.Id=Id
        
class programer(employee):
    def __init__(self,name,Id,lang):
        super().__init__(name,Id)
        
        self.lang=lang
        
rohan=employee('rohan', 499)
harry=programer('harry', 1007, 'python')
print(harry.name)
print(harry.Id)
print(harry.lang)