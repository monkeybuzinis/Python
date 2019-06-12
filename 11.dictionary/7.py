"""
Create a 5 × 5 list of numbers. Then write a program that creates a dictionary whose keys are
the numbers and whose values are the how many times the number occurs. Then print the
three most common numbers.
"""
from random import randint
matrix=[[randint(0,9) for i in range (5)] for j in range (5)]
print(matrix)

D={}
L=[]
for i in range (5):
    for j in range (5):
        L+=[matrix[i][j]]
L.sort()
print(L)


position=0

while position<len(L):
    no=L[position]
    time=L.count(L[position])
    D[no]=time

    position+=time
    
print(D)
    
    

