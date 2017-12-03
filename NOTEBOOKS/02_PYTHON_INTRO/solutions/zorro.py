
def zorro2(n):
    str="*"*n
    print (str)
    for i in range(n-2):
        nspaces=(n-i-2)
        print (" "*nspaces+"*")
    print (str)

# or you can create a string to define the format.
def zorro(n):
    str="*"*n
    print (str)
    for i in range(1,n-1):
        nspaces=(n-i)
        fmt="{:>"+"%d"%nspaces+"s}"
        print (fmt.format("*"))
    print (str)



zorro(4)
zorro(6)