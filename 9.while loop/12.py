"""In Chapter 4 there was a problem that asked you to write a program that lets the user play
Rock-Paper-Scissors against the computer. In that program there were exactly five rounds.
Rewrite the program so that it is a best 3 out of 5. That is, the first player to win three times is
the winner.
"""

list=['scissors','rock','paper']
import random

you_win=0
computer_win=0
i=0

while i<5:
    if you_win==3 or computer_win==3:
        
        if you_win==3:
            print("you win :)")
        else:
            print("you lose :(")
        break

    computer=random.choice(list)
    print("round ",i+1,":")
    yourturn=input("let's play: ")
            
    while(yourturn not in list):
        yourturn=input("oops! play again: ")
        
    else:
        if yourturn==computer:
            print("computer choice:",computer)
            print("noone win this round")

        elif((yourturn==list[0] and computer==list[2]) or (yourturn==list[1] and computer==list[0])or(yourturn==list[2] and computer==list[1])): 
            print("computer choice:",computer)
            you_win+=1
            print("you win this round")
            
        else:
            print("computer choice:",computer)
            computer_win+=1
            print("you lose this round")

        i+=1          
            
else:
    print("Final:")
    if you_win>computer_win:
        print("you WIN :)")
    elif computer_win>you_win:
        print("you LOSE :(")
    else:
        print("Noone win")
