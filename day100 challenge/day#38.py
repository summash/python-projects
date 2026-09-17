a=int(input("enter any number between 1 to 9: "))

if(a<1 or a>9):
    raise ValueError("value should be between 1 to 9")

print(a)