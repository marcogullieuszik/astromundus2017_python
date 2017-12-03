import numpy as np


v=np.random.uniform(1,10,5)
closest=v[np.argmin(np.abs(v-3))]
print (v)
print (closest)
