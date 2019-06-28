"""
You are given a file namelist.txt that contains a bunch of names. Some of the names are
a first name and a last name separated by spaces, like George Washington, while others have
a middle name, like John Quincy Adams. There are no names consisting of just one word or
more than three words. Write a program that asks the user to enter initials, like GW or JQA,
and prints all the names that match those initials. Note that initials like JA should match both
John Adams and John Quincy Adams.
"""
name1=[line.strip() for line in open ("12.textfiles/namelist.txt")]
names=[line.lower().split(' ') for line in name1]
names_initial=[[name[i][0] for i in range (len(name))] for name in names]
 
initial=input("enter initials: ")
count=0

while len(initial) not in (2,3):
    initial=input("enter initials again, initial should be 2 or 3 words: ")
else:
    if len(initial)==3:
        
        for i in range (len(names_initial)):
            if list(initial.lower())==names_initial[i]:
                print(name1[i])
                count+=1
    else:
        
        for name in names_initial:
            if len(name)==3:
                name.remove(name[1])
        
        for i in range (len(names_initial)):
            if list(initial.lower())==names_initial[i]:
                print(name1[i])
                count+=1
if count==0:
    print("sorry...there is no name matched")