

class library:
   def __init__(self,books):
       self.books=books
   def show(self):
       print(f'the books are \n"{self.books}"')
     
a=library('history of everything')
b=library('48 laws of power')
a.show()
b.show()