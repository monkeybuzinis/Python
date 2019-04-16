b=eval(input('enter the number: '))
message=input('enter a string: ')
encrypt=''
for i in range (b):
    encrypt+=message[i::b]
    print(len(message[i::b]))