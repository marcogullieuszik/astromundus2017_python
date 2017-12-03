
s="My name is Marco"

# solution 1
sol1=""
for x in s.split():
    y=x[::-1] # reverse the order
    sol1+=y
    sol1+=" " # add a space
print (sol1)

# solution 2, with list comprehensions

l=[x[::-1] for x in s.split()]
sol2=" ".join(l)
print (sol2)

# solution3 in 1 line
sol3=" ".join(x[::-1] for x in s.split())
print (sol3)