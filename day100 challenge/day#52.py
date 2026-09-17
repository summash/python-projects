#lambda functons
#def double(x):
   #return x*2

double= lambda x: x*2 #this is a lambda function
avg=lambda x , y , z , a:(x+y+z+a)/4
print(avg(2,3,4,5))
print(double(5))

#passing a function 

def appl(fx , value):
    return 6 + fx(value)

print(appl(lambda b: b*b,4))