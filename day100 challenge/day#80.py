#syntax
class base:
    pass

class derivedclass1(base):
    pass

class derivedclass2(derivedclass1):
    pass

#example
class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def showdetails(self):
        print(f'name: {self.name}')
        print(f'species: {self.species}')

class dog(animal):
    def  __init__(self,name,breed):
        animal.__init__(self, name, species='Dog')
        self.breed=breed
        
    def showdetails(self):
        animal.showdetails(self)
        print(f'breed:{self.breed}')

class goldenretriver:
    def __init__(self,name,colour):
        dog.__init__(self, name, breed='golden retriver')
        self.colour=colour
        
    def showdetails(self):
        dog.showdetails(self)
        print(f'colour: {self.colour}')
        
        
        
o=goldenretriver('tommy', 'brown')
o.showdetails()

