from glob import glob
import os
from shutil import copyfile

odir="spectra_WIN"

for f in glob("spectra/*fits"):
    f0=os.path.basename(f)
    f0=f0.replace(":","_")
    f0=f0.replace(".","_")
    f0=f0.replace("_fits",".fits")

    ff="%s/%s"%(odir,f0)

    
    copyfile(f,ff)
    
