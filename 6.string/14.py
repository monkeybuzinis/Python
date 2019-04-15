14
s=input("write your name: ")
new=''
for i in range (1,len(s)):
    if(s[i-1]==" " and s[i].isalpha()):
        new+=s[i].upper()
    else:
        new+=s[i]

if(s[0].isalpha): 
    print(s[0].upper()+new)
else:
    print(new)