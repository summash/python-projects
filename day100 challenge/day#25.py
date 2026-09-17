#tuples are imutable
#covert to list then to tuple
countries=("spain",'russia',"india","japan","finland")#tuple
temp=list(countries)#turning to list
temp.append("america")#adding a country
countries=tuple(temp)#changing to tuple
print(countries) 
#we can also concatinate a tuple
country2=('iceland',"england")
print(countries+country2)
tup=(1,2,3,4,3,4,2,1,3)
count=tup.count(3)
res=tup.index(3,5,9)
print("the count of 3 is: ",count)
print('index is: ',res)