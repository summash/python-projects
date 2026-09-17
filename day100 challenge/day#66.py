class employee:
    company_name='samsung'#this is a class variable
    noofemployees=0
    def __init__(self,name):
        self.name=name#this is a instance variable
        self.raise_amount =0.02
        employee.noofemployees+=1
    def showdetails(self):
        print(f'the name of the emplopyee is {self.name} and the raise amount is {self.raise_amount} and works in {self.company_name} sized {self.noofemployees}')
        
#employee.showdetails(emp1)
emp1=employee('yaisa')
emp1.company_name='samsung india'
emp1.showdetails()
emp2=employee('rahul')
emp2.showdetails()