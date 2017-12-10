
p=np.polyfit(Kb,JKb,1)  # K vs JK, not JK vs K !!!
Kfit=[Kb.min(),Kb.max()]

JKfit=np.polyval(p,Kfit)

ax.plot(JKfit,Kfit,lw=3,c='b')

# adjust the limits
ax.set_ylim(Kb.max(),Kb.min())

fig