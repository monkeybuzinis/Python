"""
Write a program that creates the list [1,11,111,1111,...,111...1], where the entries
have an ever increasing number of ones, with the last entry having 100 ones.
"""

L=[int("1"*i) for i in range(1,111)]
print(L)