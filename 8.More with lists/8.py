#drawing names out of the hat, entries for every name may vary

namestring=input("enter names to put in the hat, separated by space: ")

names=namestring.split(" ")

entry=[]

for c in names:
    entry+=[eval(input("enter the entry for %s: " %c ))]

hat=[]

for i in entry:
    for j in range (i):
        hat.append(names[entry.index(i)])

from random import shuffle
shuffle(hat)

from random import choice

print("the winner is: ",choice(hat))
