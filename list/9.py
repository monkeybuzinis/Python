#9

r=[]
from random import randint
for j in range (10000):
    r+=[randint(1,6)+randint(1,6)]
for i in range (2,13):
    print(i,":", r.count(i)/100,"%")
