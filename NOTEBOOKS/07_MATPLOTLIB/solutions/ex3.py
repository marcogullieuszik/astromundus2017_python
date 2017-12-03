%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def limacon(t,r0):
    r=r0+np.cos(t)
    x=r*np.cos(t)
    y=r*np.sin(t)
    return x,y

t=np.linspace(0,2*np.pi,100)
x1,y1=limacon(t,0.8)
x2,y2=limacon(t,1.0)
x3,y3=limacon(t,1.2)

fig,ax=plt.subplots()
ax.plot(x1,y1,label="$r_0=0.8$")
ax.plot(x2,y2,label="$r_0=1.0$")
ax.plot(x3,y3,label="$r_0=1.2$")
ax.legend()