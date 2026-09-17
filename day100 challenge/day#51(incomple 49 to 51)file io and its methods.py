with open('myfile1.txt' ,'r') as f:
    
    print(type(f))
    
    
    f.seek(10)
    f.tell()

#data=f.read(5)

#print(data)
