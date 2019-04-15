7
no=0
import math
n=eval(input("enter a number: "))
for i in range (2,n+1):
    if(n%i==0 and math.sqrt(i)==int(math.sqrt(i)) ):
        no=1
if(no):
    print("not squarefree")
else:
    print("squarefree") 