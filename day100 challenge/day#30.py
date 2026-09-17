def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial(n-1)#calling a function inside a function
print(factorial(int(input("enter the number: "))))

    