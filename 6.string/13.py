#13
print("enter 2 strings with same length:")
s1=input("string 1: ")
s2=input("string 2: ")
i=0
new=''
if (len(s1)==len(s2)): 
    for c in s1:
        new+=c+s2[i]
        i+=1
    print(new)
else:
    print("you didnt do as what I told")