a = [1, 12, 2, 3, 5, 8, 13, 21, 34, 55, 89]

sol1=[]
for v in a:
    if v>5 and v<15:
        sol1.append(v)
print (sol1)

# 1-line
sol2=[v for v in a if v>5 and v<15]
print (sol2)