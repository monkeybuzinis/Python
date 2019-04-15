#5 va 6
sum=0
n=eval(input("enter a number: "))
for i in range (1,n):
    if(n%i==0):
        sum=sum+i

if(n==sum):
    print(n,' is a perfect number')
else:
    print(n, 'is imperfect')