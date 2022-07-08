"""
Write a program to play the following simple game. The player starts with $100. On each
turn a coin is flipped and the player has to guess heads or tails. The player wins $9 for each
correct guess and loses $10 for each incorrect guess. The game ends either when the player
runs out of money or gets to $200.
"""
money=100
coin=["head","tail"]

guess=input("your guess: ")
g =guess.lower()
while g not in coin:
    guess=input("guess correctly please: ")
    g =guess.lower()

from random import choice
flip=choice(coin)

while money>0 and money<=200:
    if flip==g:
        money+=9
    else:
        money-=10
    print("money= ",money)
    #play again
    flip=choice(coin)
    guess=input("your guess: ")
    g=guess.lower()
    while g not in coin:
        guess=input("guess correctly please: ")
        g=guess.lower()
else:
    print("GAME END, you got: ",money)
