x=4

def hello():
    x=5
    print(f'the local x variable is {x}')
    
hello()

print(f'the global x variable is {x}')


#changing global variable through function
y=2

def func():
    global y
    y=6
    #print(y)
func()
print(y)

