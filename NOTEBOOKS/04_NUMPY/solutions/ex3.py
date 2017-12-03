import numpy as np

r = np.zeros((8,8),dtype=int)
r[1::2,::2]=1
r[::2,1::2]=1

r