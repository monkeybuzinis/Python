"""
Write a text-based version of the game Memory. The game should generate a 5 × 5 board (see
the exercise from Chapter 8). Initially the program should display the board as a 5 × 5 grid of
asterisks. The user then enters the coordinates of a cell. The program should display the grid
with the character at those coordinates now displayed. The user then enters coordinates of
another cell. The program should now display the grid with the previous character and the
new character displayed. If the two characters match, then they should permanently replace
the asterisks in those locations. Otherwise, when the user enters the next set of coordinates,
those characters should be replaced by asterisks. The game continues this way until the player
matches everything or runs out of turns. You can decide how many turns they player gets
"""
#creating the 6x6 matrix
import string
import random

L=2*random.sample(string.punctuation + string.ascii_letters,6*3) # dùng dấu '+' chứ không dùng 'and' được
random.shuffle(L)
3


memory_game=[[L[i+j*6] for i in range (6)] for j in range (6)] # cách dùng L[i+j*6] nhanh hơn

for i in range (6):
    for j in range (6):
        print(memory_game[i][j], end=" ")
    print()
print()

hidden=[["*" for i in range (6)] for j in range (6)]
turn=0

while turn<5:
    # hiển thị 6x6 *
    print("so far: ")
    for i in range (6):
        for j in range (6):
            print(hidden[i][j],end=' ')
        print()

    # lenh tao coordinator thu 1
    r1=eval(input("input the number of row of the 1st character (0=<r<6): "))
    while r1 not in range (0,6):
        r1=eval(input("wrong! the number of row of the character should be in range 0 to 6: "))
        
    c1=eval(input("input the number of column of the 1st character(0=<r<6): "))
    while c1 not in range (0,6):
        c1=eval(input("wrong! the number of column of the character should be in range 0 to 6: "))
    
    #hiển thị 6x6 * với cùng character tại vị trí đã chọn:
    hidden[r1][c1]=memory_game[r1][c1]
    
    for i in range (6):
        for j in range (6):
            print(hidden[i][j],end=" ")
        print()
    
    # lenh tao coordinator thu 2
    r2=eval(input("input the number of row of the 2nd character (0=<r<6): "))
    while r2 not in range (0,6):
        r2=eval(input("wrong! the number of row of the character should be in range 0 to 6: "))
        
    c2=eval(input("input the number of column of the 2nd character(0=<r<6): "))
    while c2 not in range (0,6):
        c2=eval(input("wrong! the number of column of the character should be in range 0 to 6: "))
    while r2==r1 and c2==c1:
        c2=eval(input("the first coordinator and the second shound be different, enter the column again: "))
    
    #hiển thị 6x6 * với cùng character tại vị trí đã chọn:
    hidden[r2][c2]=memory_game[r2][c2]
    
    for i in range (6):
        for j in range (6):
            print(hidden[i][j],end=" ")
        print()

    #lenh so sanh hai character da chon
    if memory_game[r1][c1]==memory_game[r2][c2]:
        print("congrate! you are correct")
        hidden[r1][c1]=" "
        hidden[r2][c2]=" "
    else:
        print("sorry...uncorrect")
        turn+=1
        hidden[r1][c1]="*"
        hidden[r2][c2]="*"
else:
    if hidden==memory_game:
        print("Wow, your memory is sharp")
    else:
        print("run out of time :( your memory needed to train more")
        