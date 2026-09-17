import random

def check(comp,user):
    if comp==user:
        return 0
    if(comp==0 and user==1):
        return -1
    if(comp==1 and user==2):
        return -1
    if(comp==2 and user==0):
        return -1
    if(comp==0 and user==2):
        return 1
    if(comp==1 and user==0):
        return 1
    if(comp==2 and user==1):
        return 1



user = int(input('0 for snakle 1 for water and 2 for gun: '))
comp= random.randint(0, 2)

print('user',user)
print('computer',comp)
score = check(comp,user)
if(score==0):
    print('its a draw')
elif (score == -1):
    print('you lose')
else:
    print('you won')