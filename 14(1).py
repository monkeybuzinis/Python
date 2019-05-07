#create a list consists of all palindromic numbers between 100 and 1000
#solution 1
list_no=list('0123456789')

palindromic_s=[]

no=''

k=1

for j in range(9):
    for i in list_no:
        no+=list_no[k]
        no+=i
        no+=no[0]
        palindromic_s+=[no]
        no=''
    k+=1

palindromic_no=[]

for i in palindromic_s:
    palindromic_no+=[int(i)]   # convert một string chứa ký tự số sang số int_no=int(no) (với no là string số)

print(palindromic_no)