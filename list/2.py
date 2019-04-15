#2
L=[]
import random

for i in range (20):
    L.append(random.randint(1,100))
#a
print(L)
#b
print(sum(L)/len(L))
#c
L.sort()
print(L[0],L[-1])
#d
count=0
for i in L:
    if i%2==0:
        count+=1
print(count)