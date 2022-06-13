#check whether the phone number is in correct form: abc-def-hijk or 1-abc-def-hijk (all are numbers)

no=input("enter a phone number: ")

list_valid=list('0123456789-')

valid=0

if len(no)!=len('abc-def-hijk') and len(no)!=len('1-abc-def-hijk'):
    print('Invalid1')

elif no.count('-')<2 or no.count('-')>3:
    print("Invalid2")

elif no.count('-')==2:
    if (no[3]!='-' or no[7]!='-'):
        print("Invalid3")
    else:
        for i in range (len(no)):
            if no[i] not in list_valid:
                valid+=1
        
elif (no[1]!='-' or no[5]!='-' or no[9]!='-' or no[0]!='1'):
    print('Invalid4')
else:
    for i in range (len(no)):
        if no[i] not in list_valid:
            valid+=1      
    if valid!=0:
        print("Invalid5")
    else:
        print("Valid")
