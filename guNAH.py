from random import randint
import math

# image generation capabilities

def rgbwave(w,h,fb,fg):
  t=0
  pxls=[]
  for i in range(h):
    for j in range(w):
      b=0
      pn=randint(0,1000)
      gph=0.1+0.1*math.sin(t*0.01)
      g=0 if pn>950 else int(92+90*math.sin((i+j)*fg+gph))
      r=0
      pxls.extend([r,g,b])
      pn=randint(0,1000)
      t+=1
  return bytes(pxls)

def circular(w,h,fb,fg):
  t=0
  ra=200
  pxls=[]
  cx,cy=w/2,h/2
  
  for i in range(h):
    for j in range(w):
      b=0
      pn=randint(0,1000)
      d2=(i-cx)**2+(j-cy)**2
      d=math.sqrt(d2)
      g=int(132-128*d/ra) if d2<ra*ra else int(pn/(12.5+2.5*math.sin(t*0.01)))
      r=0
      pxls.extend([r,g,b])
      pn=randint(0,1000)
      t+=1
  return bytes(pxls)
