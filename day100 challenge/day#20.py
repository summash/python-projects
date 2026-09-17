def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isgreater(a, b ):#it can also be used for if else statement
    if(a>b):
        print("first number is greater ")
    else:
        print("second number is greater or equal")
a=9
b=8
#gmean=(a*b)/(a+b) instead of writing this code again and again we use functions
calculategmean(a , b)
isgreater(a, b)

c=9
d=22
calculategmean(c, d)
isgreater(c, d)# we use the above funtion
#build in functions
