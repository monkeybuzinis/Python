#8
n=eval(input("enter an integer: "))
l=[]
for i in range (1,n):
    if n%i==0:
        l+=[i]
print(l)