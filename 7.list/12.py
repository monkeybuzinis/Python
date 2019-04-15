#12
from random import randint

l=[]
l1=[]
l0=[]

for i in range (100):
    l+=[randint(0,1)]
print(l)
for i in range (100):
    if l[i]==1:
        l1+=[i]
print(l1)
for i in range (1,len(l1)):
    l0+=[l1[i]-l1[i-1]-1]
l0.sort()
print(l0)
print("the longest run of 0 is: ",l0[-1])