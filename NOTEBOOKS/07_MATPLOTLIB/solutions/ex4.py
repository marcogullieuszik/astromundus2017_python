%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

m=10
s=3
x=np.random.normal(10,3,1000)
bins=np.arange(0,20,s/4)

fig,ax=plt.subplots()
ax.hist(x,bins=bins)
ax.axvline(m,c='k')
ax.axvline(m+s,ls="--",c='k')
ax.axvline(m-s,ls="--",c='k')