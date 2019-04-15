3
import math
n=eval(input("enter a number: "))
s=0
for i in range (1,n+1):
    s=s+1/i
print(s-math.log(n))