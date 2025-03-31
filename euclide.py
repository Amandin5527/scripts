def pgcd(a,b):return [e for e in (i for i in range(1,a+1) if a%i==0) if e in (i for i in range(1,b+1) if b%i==0)][-1]
def euclide1(a,b):
  if abs(b)>abs(a):a,b=b,a
  print("Euclide pour "+str(a)+" et "+str(b)+":")
  et=[]
  while b!=0:
    r=a%b
    print(str(a)+"="+str(b)+"x"+str(int((a-r)/b))+"+"+str(r))
    et.append((a,b,int((a-r)/b),r))
    a,b=b,r
  
  return et

def bombardement(a,b,c):
    #if abs(b)>abs(a):a,b=b,a
    
    for i in range(11):
        for j in range(11):
            #print(i,j)
            if (a*i)+(b*j)==c:
                return i,j
            elif (a*i)-(b*j)==c:
                return i,-j
            elif (b*j)-(a*i)==c:
                return -i,j
            elif (-b*j)-(a*i)==c:
                return -i,-j
    return None


def eq(a,b,c,sol=True):
  #verification
  
  p=euclide1(abs(a),abs(b))
  if len(p)==1:p=abs(a) if abs(a)<abs(b) else abs(b)
  else: p=p[-2][3]
  eqDebut=str(a)+"x"+("+" if b>0 else "")+str(b)+"y="+str(c)
  print("\ndonc PGCD({0},{1})={2}".format(abs(a),abs(b),p))
  if c%p!=0:
      print("{} ne divise pas {} -> aucune solution".format(abs(p),abs(c)))
      return
  elif p!=1:
      print("En divisant par "+str(p)+":")
      a,b,c=a//p,b//p,c//p
  eq=str(a)+"x"+("+" if b>0 else "")+str(b)+"y="+str(c)
  print(eq)
  input()
  print("RECHERCHE D'UNE SOLUTION PARTICULIERE")
  
  #euclide+calcul u et v
  test=bombardement(a,b,c)
  euc=True
  if sol==True and test!=None:
      u,v=test[0],test[1]
      print("("+str(u)+","+str(v)+") est une solution evidente")
      if abs(b)>abs(a):u,v=v,u
      euc=False
  else:
      et=euclide1(abs(a),abs(b))
      et.pop(-1)
      input()
      print("ON ISOLE LES RESTES DANS UN MEMBRE")
      for el in et:
          print(str(el[3])+"="+str(el[0])+"-"+str(el[1])+"x"+str(el[2]))
      input()
      print("ON REMONTE L'ALGORITHME")
      n=len(et)-1
      print(str(et[n][3])+"="+str(et[n][0])+"-"+str(et[n][1])+"x"+str(et[n][2]))
      u=1
      v=-et[n][2]
      terme1=et[n][0]
      terme2=et[n][1]
      for i in range(len(et)-2,-1,-1):
          terme2=[et[i][0],et[i][1],et[i][2]]
          print("1="+str(u)+"x"+str(terme1)+("-" if v<0 else "+")+str(abs(v) if v not in [-1,1] else "")+"("+str(terme2[0])+"-"+str(terme2[1])+"x"+str(terme2[2])+")")
          v,u=-(terme2[2]*v)+u,v
          terme1=terme2[0]
          terme2=terme2[1]
          print("1="+str(u)+"x"+str(terme1)+("+" if v>=0 else "-")+str(abs(v))+"x"+str(terme2))
  if abs(b)>abs(a):u,v=v,u
  if a<0 and euc==True:u=-u
  if b<0 and euc==True:v=-v
  input()
  if euc==True:
      u,v=u*c,v*c
      eq2=str(a)+"x"+str(u)+(" + " if b>=0 else "")+str(b)+"x"+str(v)+" = "+str(c)
      print("en multipliant par "+str(c)+": "+eq2)
      input()
  eq2=str(a)+"x"+str(u)+(" + " if b>=0 else "")+str(b)+"x"+str(v)+" = "+str(c)
  print("ainsi ("+str(u)+","+str(v)+") est une solution particuliere. Donc par soustraction")
  print(str(a)+"(x"+("+" if u<=0 else "")+str(-u)+(")+" if b>=0 else ")")+str(b)+"(y"+("+" if v<=0 else "")+str(-v)+")=0")
  b=-b
  #v=-v
  print("donc "+str(a)+"(x"+("+" if u<=0 else "")+str(-u)+") = " + str(b)+"(y+"+str(-v)+") Or "+str(a)+" et "+str(b)+" sont premiers entre eux")
  print("donc d'apres le thr de Gauss: "+str(a)+"|("+str(-v)+"+y) donc il existe kEZ tel que "+str(-v)+"+y="+str(a)+"k")
  
  print("On peut alors ecrire: "+str(a)+"(x"+("+" if u<=0 else "")+str(-u)+") = "+str(b)+"*"+str(a)+"k")
  print("Alors x="+str(u)+("+" if b>0 else "")+str(b)+"k on en deduit y="+str(v)+("+" if a>=0 else "")+str(a)+"k\n")
  
  
  
  print("VERIFICATION: si x="+str(u)+("+" if b>0 else "")+str(b)+"k et y="+str(v)+("+" if a>=0 else "")+str(a)+"k alors:")
  print(str(a)+"x"+("+" if b>=0 else "")+str(b)+"y="+    str(a)+"("+str(u)+("+" if b>=0 else "")+str(b)+"k"+(")+" if -b>=0 else ")")+str(-b)+"("+str(v)+("+" if a>=0 else "")+str(a)+"k)")
  print("="+str(a*u)+ ("+" if a*b>=0 else "")+str(a*b)+"k" + ("+" if -b*v>=0 else "")+str(-b*v) + ("+" if -b*a>=0 else "")+str(-b*a)+"k="+str(c))
  
  print("\nCONCLUSION: les solutions de l'equation "+eqDebut+" sont les couples\n("+str(u)+("+" if b>0 else "")+str(b)+"k,"+str(v)+("+" if a>=0 else "")+str(a)+"k) ou k entier relatif")