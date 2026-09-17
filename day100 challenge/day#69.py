class employee:
    company = 'samsung'
    def show(self):
        print(f'name: {self.name} and works in {self.company}')
    @classmethod  
    def changecompany(cls,newcompany):
        cls.company=newcompany
        
e1= employee()
e1.name ='harry'
e1.changecompany('tesla')
e1.show()
print(employee.company)