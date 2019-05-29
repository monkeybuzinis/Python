from random import randint
matrix=[[randint(0,1) for i in range (5)] for j in range (5)]

r = eval(input("enter a row with value <5: "))
c = eval(input("enter a colunm with value <5: "))

if r<5 and c<5:
    if matrix[r][c]==1:
        print("Hit")
    else:
        print("Miss")
else:
    print("you have entered wrong colunm or row")
