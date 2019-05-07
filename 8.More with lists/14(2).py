#create a list consists of all palindromic numbers between 100 and 1000
#solution 2

no=[i for i in range (100,1000)]

palindromic_no=[]

for i in no:
    if int(i/100)==i%10:
        palindromic_no.append(i)
        
print(palindromic_no)