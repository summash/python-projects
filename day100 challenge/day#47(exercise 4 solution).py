st=str(input("enter the message: "))
words=st.split(" ")
coding=input("1 for coding and 0 for decoding: ")
if(coding):
    nwords= []
    for word in words:
        if(len(st)>=3):
            r1="dwe"
            r2="fuwek"
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
    else:
        nwords.append(word[:-1])
    print(' '.join(nwords))

else:
    nwords=[] 
    if(len(words)>=3):
        r1="dwe"
        r2="fuwek"
        stnew= r1+ word[3:-3]
        stnew=stnew[-1] + stnew[:-1]
        nwords.append(stnew)
    else:
        nwords.append(word[:-1])
    print(' '.join(nwords))