string=input("enter your string: ")
letter=input("enter the letter: ")
i=0
while i<len(string) and letter!=string[i]:
    i+=1
else:
    if i==5:
        print("the string doesn't contain that letter")
    else:
        print("the string contains the letter", letter,", and the fist position of the letter is: ", i+1)