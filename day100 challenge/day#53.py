#map

def cube(x):
    return x*x*x

l=[1,2,5,7,8,9]

print(list(map(cube, l)))
#the is also another longer method using iteration i.e for loop or while loop

print(list(map(lambda x: x*x,l)))#lambda function also works

#filter 

def filter_function(a):
    return a>4

newl=list(filter(filter_function,l))

print(newl)
            
#reduce

from functools import reduce

numb=[1,2,3,4,5,6]

Sum=reduce(lambda x,y: x+y , numb)
print(Sum)
#the output is 1+2+3+4+5+6 in the list and returns a single value