questions=["what is the si unit of work done in cgs system?","erg","joules",'teri maka bhosra','none of the above',1]
           

levels=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

money=0

for i in range (0,len(questions)):
    question = questions[i]
    print(f"questions for rs.{levels[i]}")
    print(f"a. {question[1]}    b. {question[2]}")
    print(f"c. {question[3]}    d.{ question[4]}")
    reply=int(input("enter the answer: "))
    if(reply == question[-1]):
        print(f"correct answer,you have wom {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=32000
    else:
        print("padhai karle sale")
        break
    
    