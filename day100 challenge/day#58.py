#parameterized constructor <(self,argument)>

class person:
    def __init__(self,name,occ):
        #print('hey i am a person')
        self.name=name
        self.occ=occ
    def info(self):
        print(f'{self.name} is a {self.occ}')
        
a=person('yaisa','student')
b=person('divya','student')
c=person('bidyananda', 'lazy student')
a.info()
b.info()
c.info()