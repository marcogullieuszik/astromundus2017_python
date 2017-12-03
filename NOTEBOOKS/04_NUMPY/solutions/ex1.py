import numpy as np

r = np.random.random(5)
print (r)
r[np.argmax(r)] = 0

print (r)