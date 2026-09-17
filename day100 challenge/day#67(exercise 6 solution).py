class library:
    def __init__(self):
        self.nobooks=0
        self.books =[]
        
    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
        
    def showinfo(self):
        print(f'the library has {self.nobooks} books and the books are:')
        for books in self.books:
            print(books)
        
l1=library()
l1.addbook('harry potter')
l1.addbook('48 laws of power')
l1.addbook('rd sharma maths class 11')
l1.addbook('rich dad poor dad')
l1.showinfo()