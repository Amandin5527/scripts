def pi(n):return(-1)**(n%2)*4/(2*n+1)+pi(n-1)if n>0 else 4
def factorial(n):return 1 if n==1 else n*factorial(n-1)
def fusion(t1, t2):return (t1 and t2 and [t1.pop(0) if t1[0] < t2[0] else t2.pop(0)] + fusion(t1, t2)) or t1 + t2
def tri_fusion(tab):return fusion(tri_fusion(tab[:len(tab)//2]),tri_fusion(tab[len(tab)//2:]))if len(tab)>1 else tab

def additionListe(L1,L2,D=100,T=5):
    for i in range(D):
        v = L1[i]+L2[i]
        if v>10**T and i>0:L1[i-1]+=1
        L1[i]=v%10**T
    return L1
#print(additionListe([11111,22222,33333,77777,88888],[123,22224,21556,25558,44512]))


#TOUTES LES FONCTIONS PR CALCULER PLEIN DE DECIMALES ED PI
def unSur(d,D=100,T=5):
    L=[0]*D #k
    n=1 #denominateur (C LE MEME DENO)
    for i in range(D):#nombre de paquets de m chiffres
        for j in range(T): #nombre de chiffre dans un paquet
            q = n//d
            L[i]*=10 #ca decale tt vers la gauche
            L[i]+=q #ca ajoute le quotient
            n = (n-q*d)*10
    return L

def arctan(x,n,D=100,T=5): #x=1/x et n=nbr de termes (sa devient de + en + precis)
    L = [0]*D
    c=x*x
    p = 1 #puissance de x dans le terme de la série
    for i in range(n):
        L = additionListe(L, unSur(p*x))
        p+=2
        if x<0:L[D-1]+=1
        x*=-c
    return L

def aff(r,D=100,T=5):
    """affiche la liste sans les paquets"""
    for i in range(D):
        print(("0"*T + str(r[i]))[-T:],end="")
    
    
#aff(unSur(239))

#PROGRAMME DE PI FINAL!!!
D,T=100,5 #D paquets de T chiffres
def pi_decimales():
    v=arctan(5,360)
    w=arctan(-239,110)
    L=additionListe(v,v)
    L=additionListe(L,L)
    L=additionListe(L,w)
    L=additionListe(L,L)
    L=additionListe(L,L)
    aff(L)
pi_decimales()