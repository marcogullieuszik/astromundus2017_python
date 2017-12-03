
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

y,x=np.mgrid[0:800,0:800]

s=50
xc=300
yc=400

r2=(x-xc)**2+(y-yc)**2

z=np.exp(-.5*r2/s**2)

fig,ax=plt.subplots()
ax.imshow(z,origin='lower')