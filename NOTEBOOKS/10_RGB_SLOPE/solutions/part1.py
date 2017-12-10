
cname="M15"
# create a condition to select only data for one cluster
cond=catalog["GlCl"]==cname

# select the columns with J and K-band magnitudes and get only data for your cluster
J=catalog["Jmag"][cond]
K=catalog["Kmag"][cond]
JK=J-K

# create a condition to select only the brightest stars 
Klim=K.min()
cond_bright = (K<Klim+5) & (K>Klim+.5) 

Kb=K[cond_bright]
Jb=J[cond_bright]
JKb=Jb-Kb

# plot the CMD
fig,ax=plt.subplots(figsize=(6,8))
ax.plot(JK,K,'.k',ms=2)
ax.plot(JKb,Kb,'.r',ms=2)
# adjust the limits
ax.set_xlim(-.9,2.2)
ax.set_ylim(16,9)
ax.set_xlabel("J")
ax.set_ylabel("J-K");