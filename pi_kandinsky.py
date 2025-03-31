#numworks
from math import *
from kandinsky import *

def pipi(n):
  piv=0
  coun=0
  x=1
  fill_rect(56,16,208,28,"black")
  fill_rect(60,20,200,20,"white")
  der=int(n/100) if n>100 else 1
  for i in range(n+1 if n>100 else n):
    piv+=4/x-4/(x+2)
    x+=4
    if (i)%der==0:
      coun=i+1
      text=str(floor((coun/n)*100))+"%"
      draw_string(text,140,50)
      fill_rect(0,80,320,22,"white")
      draw_string("temps restant:"+(str(int((n-i)*9/10**7)+1) if n-i>1111111 else "moins de 1")+" minutes",0,80)
      fill_rect(60,20,floor((coun/n)*200),20,"green")
  fill_rect(0,80,320,22,"white")
  draw_string("fini",50,80)
  draw_string(str(piv),50,100)
  diff=str((piv/pi)*100)+"%"
  draw_string("% de similitude avec pi",50,120)
  draw_string(diff,50,150)
