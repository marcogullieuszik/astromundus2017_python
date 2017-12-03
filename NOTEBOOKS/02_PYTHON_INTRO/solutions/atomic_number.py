
l=sorted(Z.keys())
mNe=Z["Ne"]
for element in l:
    if Z[element]<mNe:
        print ("Element: {0:2s} - atomic mass: {1:>2d}".format(element,Z[element]))