class math:
    def __init__(self,num):
        self.num=num
    def addtonum(self, n):
        self.num=self.num + n 
        
    @staticmethod
    def add(a, b):
        return a + b
    
a=math(5)
a.addtonum(5)
print(a.num)
print(math.add(2, 3))#static method dont require any instance or class methods