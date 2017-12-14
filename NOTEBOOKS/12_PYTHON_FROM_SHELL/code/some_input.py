import matplotlib.pyplot as plt
import numpy as np
import sys

args=sys.argv # get the arguments

print("starting...")
print (args)

s=args[1]

x=np.linspace(-1,3,100)
y=x**2+2*x

fig,ax=plt.subplots()

ax.plot(x,y)
ax.set_title(s)
fig.savefig("some_input_fig.png")
print ("DONE")
