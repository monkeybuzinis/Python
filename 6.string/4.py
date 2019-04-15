#4
v="aeuio"
s=input("enter a string: ")
a=0
for i in range(5):
    if(v[i] in s):
        a=1
if(a):
    print("yes")
else:
    print("no")
