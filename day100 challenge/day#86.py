numbers=[1,2,3,4,5]

while (n:= len(numbers)) > 0:
    print(numbers.pop())
    
    


happy = False
print(happy)

print(happy := True)


foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)    