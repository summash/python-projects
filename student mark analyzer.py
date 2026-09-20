import pandas as pd
#lets make a student mark analyser 

#Topper of the class

#Students who failed/passed

#Subject-wise performance

#adding marks and new students and deleting and or modifying students

#input
user=input("""what is your command sir:
               1.display topper of ther class 
               2.print avg of a student
               3.display pass or fail
               """)


#data as a dict 
data={
      'name':["yaiyai","alice",'ana','jake'],
      'marks':[99,78,87,78,]
      }
#saving the dict as a dataframe
df=pd.DataFrame(data)


#prints the dataframe
#print(df)


#saves the file as an csv file
#df.to_csv('output.csv', index=False) 

#topper of class
def topper():
    highest=max(data.values())
    print(highest)
    
#average marks 
#def avg():
    
#students who failed or passed
#def Pass_fail():
    
#input and output
if user=="display topper of class" or "1" or 1:
    topper()