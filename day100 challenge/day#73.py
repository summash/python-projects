class employee:
    name='name'
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
            return i
    
e=employee()
print(e.name)
print(len(e))

from emp import employee 

e = employee('harry')
print(str(e))
print(repr(e))
e()