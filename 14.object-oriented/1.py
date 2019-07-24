"""
Write a class called Investment with fields called principal and interest. The constructor should set the values of those fields. 
There should be a method called value_after that returns the value of the investment after n years. 
The formula for this is p(1 + i)n
, where p is the principal, and i is the interest rate. 
It should also use the special method __str__ so that
printing the object will result in something like below:
    Principal - $1000.00, Interest rate - 5.12%
"""

class Investment:
    def __init__(self,name,principal,interest):
        self.name=name
        self.principal=principal
        self.interest=interest
    def __str__(self):
        return "Principal-{}, Interest rate-{}".format(self.principal,self.interest)
    def value_after(self,n):
        value=self.principal*(1+self.interest)**n 
        return "After {} years, {} will get {}$".format(n,self.name,value)
Khanh=Investment("Khanh",100000,0.05)
print(str(Khanh))
print(Khanh.value_after(3))
