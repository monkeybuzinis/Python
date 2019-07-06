"""
(a) Write a function called primes that is given a number n and returns a list of the first n
primes. Let the default value of n be 100.
(b) Modify the function above so that there is an optional argument called start that allows
the list to start at a value other than 2. The function should return the first n primes that
are greater than or equal to start. The default value of start should be 2.
"""
def check_prime(x):
    if x not in [1,2]:
        i=2
        while x%i!=0 and i<x:
            i+=1
        if i==x:
            return 1
        else:
            return 0
    else:
        return 1

def primes(start,n):
    
    prime_n=[]
    for i in range (start,(n+1)):
        if check_prime(i)==1:
            prime_n+=[i]
    return prime_n

n=eval(input("enter n: "))
start=eval(input("enter the starting number: "))
print(primes(start,n))


        