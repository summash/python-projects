
#dir()
x=[1,1,2]
print(dir(x))
print(x.__add__)

#__dict__

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p=person('john', 21)
print(p.__dict__)

print(help(str))