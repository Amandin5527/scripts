from random import randint
def de(a):
    p,f=0,0
    for i in range(a):
        b = randint(0,1)
        if b==0:p+=1
        else: f+=1
    print("proba pile: ",p/(p+f)*100," %")
    print("proba face: ",f/(p+f)*100," %")