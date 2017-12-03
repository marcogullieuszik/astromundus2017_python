divisors=lambda n :[i for i in range(1,n+1)
                    if n%i==0]

n=input("Enter a number ")
n=int(n)

d=divisors(n)
is_prime=len(d)==2 # a prime number has only 2 divisors: 1 and itself
if is_prime:
    print ("%d is prime"%n)
else: 
    print ("%s is not prime"%n)