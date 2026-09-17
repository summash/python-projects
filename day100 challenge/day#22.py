#list
marks=["harry=",2,3,5,3,9,4,5]#list are enclosed with square bracket and separated with commas 
#there can also be strings and boolean
print("the marks are:",marks)
print(marks[0])#it will print 2 as it is the first item in the list
#negative index
print(marks[-2])
if 2 in marks:#if else statement
    print("yes")
else:
    print("no")
#same thing applies for string as well
#range
print(marks[1: 3])
print(marks[1:2:4])
lst=[i for i in range( 1,10)]
print(lst)

