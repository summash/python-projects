#inheritence
class employee:
    def __init__(self,name,Id):
        self.name=name
        self.Id= Id
        
    def showdateails(self):
        print(f'the name of employee is {self.name} and his/her id is {self.Id}')
        
class programmer(employee):
    def language(self):
        print('default language is python')
        
        
class gender(programmer(self,gender)):
    def __init__(self,gender):
        self.gender=gender 
        
    def showgender(self):
        if gender=='male':
            print('he is a male')
        if gender=='female':
            print('she is a female')
            
        




e=employee('rohan das', 1)
e=gender('male')
e.showgender()
e.showdateails()
e1=programmer('harry',2)
e1.language()

