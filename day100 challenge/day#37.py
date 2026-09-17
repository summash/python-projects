def funct():
    try:
        l=[1,2,3,4,5]
        i=int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("always executed")#will exuct always even in a function
        
x=funct()
print(x)