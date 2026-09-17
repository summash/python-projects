name=str(input("what is your name: "))
country=str(input("where do you live: "))
letter="my name is {} and i live in {}"
print(letter.format(name, country))
letter1="my name is {1} and i live in {0}"#we can also assign like this
print(letter1.format(country, name))
#f string
print(f"hey i am {name} and i am from {country}")#{{name}} if you dont want the variable to be replaced
price=49.099999
txt=f"for only {price:.2f} dollars!!"
print(txt)#we can take only 2 decimal places like this
print(type(f"{2*30}"))#will print 60 but as a string not a integer

