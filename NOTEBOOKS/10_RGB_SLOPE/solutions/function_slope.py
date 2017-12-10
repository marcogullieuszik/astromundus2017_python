import os

odir="figures_fit"
if not os.path.isdir(odir):os.makedirs(odir)

def get_slope(cname):
    ofig="%s/plot_%s.png"%(odir,cname)
    cond=catalog["GlCl"]==cname

    # select the columns with J and K-band magnitudes and get only data for your cluster
    J=catalog["Jmag"][cond]
    K=catalog["Kmag"][cond]

    JK=J-K

    # create a condition to select only the brightest stars (5 mags in K)
    # the brighest star has a magnitude = K.min(), therefore
    Klim=K.min()
    cond_bright = (K<Klim+5) & (K>Klim+.5) 

    Kb=K[cond_bright]
    Jb=J[cond_bright]
    JKb=Jb-Kb

    p=np.polyfit(Kb,JKb,1)
    Kfit=[Kb.min(),Kb.max()]

    JKfit=np.polyval(p,Kfit)

    # plot the CMD
    fig,ax=plt.subplots(figsize=(6,8))
    ax.plot(JKb,Kb,'.k',ms=2)
    ax.plot(JKfit,Kfit)

    # adjust the limits
    ax.set_ylim(Kb.max(),Kb.min())
    ax.set_xlabel("J")
    ax.set_ylabel("J-K");
    fig.savefig(ofig)
    plt.close(fig)    ############ close the figure!!

    return p[0]