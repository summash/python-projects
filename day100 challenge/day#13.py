a="Harry"
print(a)#it makes a new variable "a.upper
print(a.upper())#python is imutable
print(a.lower())#it will create a new string from the existing string
b="yaisa !!!!"
c="introduction to my python programme"
print(b.rstrip('!'))#used for stripping down a string
print(a.replace("Harry", "yaisana"))#used to replace 
print(b.split(" "))
#print(c.capitalise())#converts the first letter to uppercase
print(c.count("my"))
print(a.endswith("y"))#give output in bool literals, used to find wheter the
print(a.startswith("H"))#same as endswith() but checks the prefix
#string ends with the word
print(a.endswith("r",2,4))#spliting the endswith 
d="he is a good man but is quite stupid"
print(d.find("is"))#used to find a specific word
print(d.index("is"))#same but will give an error if the word is onot there
print(d.isalnum())#boolean and checks alphabet with numbers
print(d.isalpha())#boolean and checks only alphabets
print(d.islower())#boolean and checks if the string is in lower case
print(d.isupper())#checks for upper case 
print(d.isprintable())#checks if the string is printable
#white space with tab or spacebar
white_space="hello  everyone    "
print(white_space.isspace())#checks white space
print(d.istitle())#checks if the string is a title
print(c.swapcase())#swaps uppercase to lowercase and vice versa
print(d.title())#converts into title i.e converts the firts letter to capital and the remaining to lowercase





