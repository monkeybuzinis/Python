#c
message=input('enter your message: ')
b=eval(input('enter the number that you want your message to be broken into: '))

encrypt=''
for i in range (b):
    encrypt+=message[i::b]
 
print("\nI bet you know what I wrote: ",encrypt)

#d
n=len(encrypt)%b
decrypt=''
if n>0:
    for j in range (int(len(encrypt)/b)):
        k=0
        decrypt+=encrypt[j]
        for i in range (b-1):
            decrypt+=encrypt[len(encrypt[i::b])+k+j]
            k+=len(encrypt[i::b])
    k=0
    for i in range (n):
        decrypt+=encrypt[len(encrypt[i::b])-1+k]
        k+=len(encrypt[i::b])
else:
    for j in range (int(len(encrypt)/b)):
        k=0
        decrypt+=encrypt[j]
        for i in range (b-1):
            decrypt+=encrypt[len(encrypt[i::b])+k+j]
            k+=len(encrypt[i::b])

print('\nI dont think it is difficult! It is: ',decrypt)