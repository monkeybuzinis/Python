# Write a sencoring program to hide all the cruse words from the enter text

curse=['darn','dang','freakin','heck','shoot']

text=input("enter some text: ")

copy=text

from string import punctuation
for c in punctuation:
    copy=copy.replace(c,'')

list_text=copy.split(' ')

for word in list_text:
    if word in curse:
        list_text[list_text.index(word)]=len(word)*'*' # replace item at index(word)
        
copy=' '.join(list_text)

for i in range (len(text)):
    if text[i] in punctuation:
        copy=copy[:i]+text[i]+copy[i:]  # way to insert into string

print(copy)
        