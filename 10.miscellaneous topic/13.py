"""
 The number 99 has the property that if we multiply its digits together and then add the sum
of its digits to that, we get back to 99. That is, (9 × 9) + (9 + 9) = 99. Write a program to find
all of the numbers less than 10000 with this property. (There are only nine of them.)
"""
for i in range (0,100):
    l=[int(j) for j in list(str(i))]
    multi=1
    for j in l:
        multi*=j
    if sum(l)+multi==i:
        print(i)
    
