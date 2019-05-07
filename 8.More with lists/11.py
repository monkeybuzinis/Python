#find an anagram of a string using random.choice

s=input("enter a string: ")

list_s=list(s)

index=[]

for i in range (0,len(s)):
    index+=[i]

from random import choice

anagram=''

for j in range (len(s)):
    i=choice(index)
    anagram+=list_s[i]
    del index[len(index)-1]
    del list_s[i]

print("an anagram of",s,"is: ",anagram)



