
# solution1
def divisors1(n):
    res=[]
    for i in range(1,n+1):
            if n % i == 0:
                res.append(i)
                
    return res

#solution2
divisors2=lambda n :[i for i in range(1,n+1)
                    if n%i==0]

## 
print (divisors1(6))
print (divisors1(24))

print (divisors2(6))
print (divisors2(24))