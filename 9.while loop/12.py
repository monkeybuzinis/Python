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

while i<3:
    computer=random.choice(list)
    print(i+1,":")
    yourturn=input("let's play: ")
    while(yourturn==computer or yourturn not in list):
        yourturn=input("oops! play again: ")
    if((yourturn==list[0] and computer==list[2]) or (yourturn==list[1] and computer==list[0])or(yourturn==list[2] and computer==list[1])): 
        you_win+=1
        i+=1
    else:
        computer_win+=1
        i+=1
else:
    print()
    if you_win>computer_win:
        print("you WIN :)")
    else:
        print("you LOSE :(")