password="abc123"
password_enter=input("enter your password: ")
i=0

while password_enter!=password and i<4:
    print("wrong! you have only", 4-i,"tries left")
    password_enter=input("reenter your password:") 
    i+=1
    
else:
    if i<4:
        print("Welcome! you have logged into the system")
    else:
        print("you are kicked out!")

