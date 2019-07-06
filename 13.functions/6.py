"""
Write a function called binom that takes two integers n and k and returns the binomial coefficient
"""

def binoma (n,k):
    from math import factorial
    print(factorial(n)/factorial(k)*1/factorial(n-k))
n=eval(input("n= "))
k=eval(input("k= "))
binoma(n,k)