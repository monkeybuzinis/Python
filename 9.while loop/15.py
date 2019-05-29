"""
Write a program to play the following game. There is a list of several country names and the
program randomly picks one. The player then has to guess letters in the word one at a time.
Before each guess the country name is displayed with correctly guessed letters filled in and
the rest of the letters represented with dashes. For instance, if the country is Canada and the
player has correctly guessed a, d, and n, the program would display -ana-da. The program
should continue until the player either guesses all of the letters of the word or gets five letters
wrong
"""
country=["canada","america","vietnam","mexico","france","thailand","australia"]

from random import choice
i=0
list_word=[]


computer_guess=choice(country)

display="-"*len(computer_guess)

while i<5 and display!=computer_guess:
    print(display)
    your_guess=input("guess a word: ")
    if your_guess in computer_guess:
        list_word+=your_guess
        display=""
        for j in range (len(computer_guess)):
            if computer_guess[j] not in list_word:
                display+="-"
            else:
                display+=computer_guess[j]       
    else:
        i+=1
        print("you have",5-i,"time(s) to guess wrong")      
else:
    if display==computer_guess:
        print("congrate! you are correct! that country is: ", computer_guess)
    else:
        print("you lose")
    