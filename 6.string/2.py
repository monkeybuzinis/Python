#2
s=input("write a sentence: ")
print(len(s))
count=0
for i in range (0,len(s)-1):
    if(s[i]==" " and s[i+1].isalpha()):
        count=count+1
if s[0].isalpha():
    print("number of words in your sentence: ",count+1)
else: 
    print("number of words in your sentence: ",count)