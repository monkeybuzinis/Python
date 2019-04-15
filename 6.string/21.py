#21
s=input("enter a word: ")
import random
for i in range (len(s)):
    j=random.randint(0,(len(s)-1))
    print(s[j],end='')
    s=s.replace(s[j],'')