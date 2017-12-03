x=np.random.uniform(3,7,1000)
perc=np.percentile(x,80)
print ("The 80-th percentile is ",perc)

cond=x<perc
below=x[cond] #select elements <perc

n=len(below) # number of elements <perc
tot=len(x)   # nubmner of elements of x
f=(n/tot) # calculate the fraction of elements <perc
print ("the fraction of elements smaller then this value is:",f)