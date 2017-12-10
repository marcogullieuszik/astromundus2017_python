
date=tab["year"]
dt=tab["dT"]
dt5=tab["dT_5"]


fig,ax=plt.subplots(figsize=(8,6))
ax.plot(date,dt,c=(.5,.5,.5),label="annual mean")
ax.plot(date,dt5,'r',lw=3,label="5 year mean")

ax.set_xlabel("year")
ax.set_ylabel("Temperature anomaly [C]")

# select only temperature after 1970
cond=(date>1970)
x=date[cond]
y=dt[cond]

# make the fit with a straight line
p=np.polyfit(x,y,1)
# evaluate the fit
yfit=np.polyval(p,x)

print("The temperature is increasing by %.3f degrees per year since 1970"%p[0])
# plot the fit
ax.plot(x,yfit,'g',lw=10,alpha=.6,label="fit") # alpha set the transparency of the line

ax.legend(frameon=False,borderpad=1,handletextpad=2);