class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(cls, string):
        return cls(string.split('-')[0], int(string.split('-') [1]))
e=employee('yaisa', 10)
print(e.name,e.salary)
string= 'john - 12000'
#e=employee(string.split('-')[0], string.split('-') [1])
e=employee.fromstr(string)
print(e.name,e.salary)
