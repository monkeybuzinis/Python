#13
from random import randint
l=[]
for i in range (10):
        l+=[randint(0,5)]
print(l)
l.reverse()
for j in range (len(l)):
        for i in l:
                if l.count(i)>1:
                        l.remove(i)
l.reverse()
print(l)