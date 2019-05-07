sentence=input("enter a sentence without punctuations: ")

list_s=sentence.split(' ')

#a
list_a=[]

for s in list_s:
    list_a+=[s[1:]]
print(list_a)


#b
list_b=[]

for s in list_s:
    list_b+=[len(s)]

print(list_b)

#c
list_c=[]

for s in list_s:
    if len(s)>=3:
        list_c+=[s]
print(list_c)
