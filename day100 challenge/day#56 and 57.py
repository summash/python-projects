class person:
    name='yai yai'
    hobby=['boxing','guitar','drawing','calisthenics']
    networth=0
    def info(self):
        print(f"{self.name} likes {self.hobby}")
        
a=person()
b=person()
c=person()

a.name='bidyananda'
a.hobby='gaming'
b.name='yaisa'
c.name='nikita'
c.hobby='dancing'

a.info()
b.info()
c.info()
#print(a.name ,a.hobby)
