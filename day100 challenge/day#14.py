a=int(input("what is your age: "))
print("your age is:",a)
if(a>=18):
    print("you can drive")
else:
    print("you are underaged")#the spcace is used to tell if we are in the if else statement
print("no")#we are not in the if else statement
#conditional operators
#<,>,<=,>=,==,!=
print(a>18)
print(a>=18)
print(a<=18)
print(a<18)
print(a==18)
print(a!=18)#boolean and will print true or false
#elif statements
num=int(input("enter the number: "))
if(num>0):
    print("number is positive")
elif(num==0):
    print("number is zero")
elif(num==-1):
    print("number is complex")
else:
    print("number is negative")
#nested if statements
x=int(input("what is the number: "))
if(x<0):
    print("number is negative")
elif(x>0):
    if(x<=10):
        print("number lies between 1 and 10")
    elif(10<x<=20):
        print("number lies between 11 and 20")
    else:
        print("number is greate than 20")
else:
    print("number is zero")
        