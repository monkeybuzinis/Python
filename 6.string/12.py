#12
s=input("enter a string: ")
new=''
s2=s[1::2].upper()
i=0
for c in s2:
     new+=s[i]+c
     i+=2
if len(s)%2==0:
    print(new)
else: print(new+s[-1])
