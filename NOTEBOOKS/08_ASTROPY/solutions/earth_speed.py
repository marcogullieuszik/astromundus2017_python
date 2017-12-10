v1=np.sqrt(const.G*const.M_sun/const.au).to(u.km/u.s)
print (v1)

# circumference / 1 year
v2=(2*np.pi*const.au/u.year).to(u.km/u.s)
print (v2)

diff=(v2-v1)/v2*100
print ("The difference is %.3f%%"%diff) # note that you need "%%" to print "%"