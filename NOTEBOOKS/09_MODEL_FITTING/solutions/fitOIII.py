
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

from astropy.io import fits
from astropy.table import Table
from astropy.modeling import models,fitting

fitsfile="data/sdss_spec-0502-51957-0007.fits"
data=fits.getdata(fitsfile,1)
tab=Table(data)


w=tab["WAVE"].data
f=tab["FLUX"].data

w_0=5008.240   # restframe [OIII]
z_sdss=0.14691 # redshift value measured by sdss

# select around the [OIII]
cond=np.abs(w-w_0*(1+z_sdss))<20
xx=w[cond]
yy=f[cond]

# 1st guess of the line center
wl=xx[np.argmax(yy)]

# model
f1=models.Gaussian1D(amplitude=1000,mean=wl,stddev=2)
f2=models.Linear1D(0,0)
fit_init=f1+f2

# fitter
fitter=fitting.LevMarLSQFitter()

# fit data
fit=fitter(fit_init,xx,yy)

# create the best-fit line
xfit=np.linspace(xx.min(),xx.max(),200)
yfit=fit(xfit)

w_m=fit.mean_0
z_m=(w_m-w_0)/w_0
print ("z=",z_m)

# plot
fig,axes=plt.subplots(2,1,figsize=(7,10))

axes[0].plot(w,f)
axes[0].plot(xx,yy,'r')
axes[0].set_xlim(4800*(1+z_sdss),5050*(1+z_sdss))

axes[1].plot(xx,yy,'r')
axes[1].plot(xfit,yfit,'k')
axes[1].set_xlim(xx.min(),xx.max());