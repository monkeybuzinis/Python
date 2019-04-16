 #22
 # a
s=input("enter a string: ")
v=s[0::2]+s[1::2]
print(v)
#b
i=0
n=''
for c in v[:int(len(v)/2)]:
    if len(v)%2==0:
        n+=c+v[int(len(v)/2)+i]
    else:
        n+=c+v[int(len(v)/2)+1+i]
    i+=1
if len(v)%2==0:
    print(n)
else: 
    print(n+v[int(len(v)/2)])
    
