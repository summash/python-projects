import time
def usingwhile():
    i=0
    while i>5000:
        print(i+1)

def usingfor():
    for i in range(5000):
        print(i)
        
        
init=time.time() 
usingfor()
t1= time.time() - init 
init=time.time()
usingwhile()
print(time.time()-init)
print(t1)


time.sleep(3)
print('this is printed after 3 secs')