import matplotlib.pyplot as plt
import numpy as np

print("starting...")
x=np.linspace(-1,3,100)
y=x**2+2*x

fig,ax=plt.subplots()

ax.plot(x,y)

fig.savefig("simple_code_fig.png")
print ("DONE")
