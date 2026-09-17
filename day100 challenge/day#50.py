f=open('myfile.txt','r')
while True:
    line=f.readlines()
    print(line)
    if not line:
        break
    print(line)
    
    
#writelines method
f=open('hello everyone.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close
