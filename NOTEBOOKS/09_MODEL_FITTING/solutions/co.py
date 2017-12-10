
date=tab["date"]
co2=tab["co2"]
co2t=tab["trend"]

fig,ax=plt.subplots(figsize=(8,6))

ax.plot(date,co2,c=(.5,.5,.5),label="data")
ax.plot(date,co2t,'r',lw=3,label="av. seasonal cycle removed")
ax.set_xlabel("year")
ax.set_ylabel("CO2 [ppm]")

p=np.polyfit(date,co2t,2)
yfit=np.polyval(p,date)

ax.plot(date,yfit,'g',lw=10,alpha=.6,label="fit") # alpha set the transparency of the line
ax.legend(frameon=False,borderpad=1,handletextpad=2);
fig.savefig("solutions/co.png")