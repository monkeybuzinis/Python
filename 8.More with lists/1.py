message=input("enter your text: ")
article=['a','an','the']

message.lower()
from string import punctuation
for c in punctuation:
    message.replace(c,'')

l=message.split()
count=0
for word in l:
    if word in article:
        count+=1
print("there are",count,"article(s) in your text")