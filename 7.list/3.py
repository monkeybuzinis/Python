#3
l=[8,9,10]
#a
l[1]=17
#b
for i in [4,5,6]:
    l.append(i)
#c
l.remove(l[0])   

#d
l.sort()
#e
l=l*2
#f
l[3]=25
print(l)