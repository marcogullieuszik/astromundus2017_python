%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi)
y=2*np.sin(x)
cond=y<1
fig,ax=plt.subplots()
ax.plot(x[cond],y[cond],'ok')
ax.plot(x[~cond],y[~cond],'^r')