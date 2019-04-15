#a one-time pad
from random import randint
abc='abcdefghijklmnopqrstuvwxyz'

message=input("enter a message: ")
message=message.lower()

encrypt=''

key=[]

for i in range (len(message)):
    if message[i].isalpha():
        j=randint(1,100)
        key+=[j]
        encrypt+=abc[(abc.index(message[i])+j)%26]
    else:
        encrypt+=message[i]

print(key)
print(encrypt)

#b
decrypt=''
n=0

for i in range (len(encrypt)):
    if encrypt[i].isalpha():   
        decrypt+=abc[(abc.index(encrypt[i])-key[n])%26]
        n+=1
    else:
        decrypt+=encrypt[i]

print(decrypt)

