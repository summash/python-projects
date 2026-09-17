x=int(input("enter the number: "))
match x:
    case 0:
        print("x is zero")#x is the variable to match
        #case with if else statement
    case 4:
        print("x is four")
    case _ if x!=90:
        print(x,"is not 90")
    case _:
        print(x)
    
