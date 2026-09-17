#'is' vs '=='
a=[1,2,43]
b=[1,2,43]

print(a==b)#value
print(a is b)#exact location of the object

print('since 3 is a constant it will  print true,\nany immutable object will give the same output')

a=3
b=3
print(a==b)
print(a is b)

