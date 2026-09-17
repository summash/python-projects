for i in range(1,13):
    print("5 x",i,"=",5*i)
    if(i==6):
        break#when i=6 it breaks the loop
print("loop ko chor nikhal gaya")
#continue 
for i in range(1,13):
    if(i==6):
        print("skip the iteration")
        continue
    print("5 x",i,"=",5*i)
#do while loop
i=0
while True:
    print(i)
    i=i+i
    if(i%100==0):
        break
    
    

