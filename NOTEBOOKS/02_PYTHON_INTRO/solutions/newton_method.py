# define the function and the derivative
def f(x):
    return x**3-3*x**2 -3*x+9
def df(x):
    return 3*x**2-6*x-3

# define a function to calculate the "distance from zero"
def dx(x):
    return abs(0-f(x))

tolerance=1.0e-7 # stop when dx<tolerance!

x0=0.1# our fist guess
delta=dx(x0)
while delta >=tolerance:
    #fill in the blanks using the first equation!
    x0= x0 - f(x0)/df(x0)
    #then fill in the blank with your new delta from your new x0
    delta = dx(x0)
    
print (x0)
print (f(x0))