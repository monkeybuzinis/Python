23
#c
b=eval(input('enter the number: '))
s=input('enter a string: ')
v=''
for i in range (b):
    v+=s[i::b]
print("your encrypted message: ",v)
#d
n=''
if len(s)%b==0:
    for j in range ((int(len(s)/b)+1)):
        for i in range (b):
            n+=v[i:len(s):b]
        v=n
        n=''
        print(v)
else:
    for j in range ((int(len(s)/b)+2)):
        for i in range (b):
            n+=v[i:len(s):b]
        v=n
        n=''
        print(v)
