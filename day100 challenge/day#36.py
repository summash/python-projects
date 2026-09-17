a=input('enter the number: ')
print(f"multiplication of {a} is: ")

try:
    for i in range(1,11):
        print(f"{a}x{i}=",int(a)*i)#if we enter a number which is not an integer then it will skip to the last line
        #if we do this then the program will not hault
except:
  print("sorry some error occurred")  

print("most important line")
print("end of code")
