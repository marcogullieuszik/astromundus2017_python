import random
ngames=1000
won=0
for i in range(ngames):
    res=random.randint(1,6)
    if res==2 or res==4: won+=1

print ("I won %s times"%won)
p=100*won/ngames
print (p)