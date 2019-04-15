10
l=eval(input())
s=l[:]
for i in range (len(l)):
    s[i]=l[(len(l)-1+i)%len(l)]
print(s)