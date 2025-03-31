from math import sqrt
from random import uniform
def pi(N=100):
    cercle=0
    for i in range(N):
        pt = [uniform(-1, 1) for zgeg in range(2)]
        if sqrt(pt[0]**2+pt[1]**2)<=1:cercle+=1
    return 4*cercle/N



def cercle(N_iterations=100):
    
    R = 1
    progY = 0
    progX = R
    AC = 0
    H = R/N_iterations
    longueur = 0
    longueurArc = 0
    
    
    for i in range(N_iterations):
        if R**2 - (progY+H)**2 > 0:
            progY += H
            AC = sqrt(R**2 - progY**2)
            longueur = sqrt(H**2 + (progX-AC)**2)
            progX = AC
            longueurArc+=longueur
        
    reste = R-progY
    longueurArc += sqrt(progX**2 + reste**2)
        
    cercleComplet = 4*longueurArc
    return cercleComplet/(2*R)