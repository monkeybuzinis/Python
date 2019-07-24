"""
Write a class called Rock_paper_scissors that implements the logic of the game Rockpaper-scissors. 
For this game the user plays against the computer for a certain number of
rounds. Your class should have fields for the how many rounds there will be, the current
round number, and the number of wins each player has. There should be methods for getting
the computer’s choice, finding the winner of a round, and checking to see if someone has one
the (entire) game. You may want more methods.
"""
class Rock_paper_scissors:
    def __init__(self,round_number):
        self.round_number=round_number
        self.current_round=0
        self.your_win_number=0
        self.computer_win=0
        self.L=["rock","paper","scissors"]

    def computer_choice(self):       
        from random import choice
        computer_choice=choice(self.L)
        return computer_choice

    def your_choice(self,t_f):
        if t_f==True:
            your_choice=input("your turn: ")         
        else:
            your_choice=input("play again: ")
        return your_choice
    def action(self):
        win=[[self.L[0],self.L[2]],[self.L[1],self.L[0]],[self.L[2],self.L[1]]]

        while self.current_round<self.round_number:
            computer_choice=self.computer_choice()
            your_choice=self.your_choice(True)

            while your_choice==computer_choice or your_choice not in self.L: 
                computer_choice=self.computer_choice()
                your_choice=self.your_choice(False)
                          
            if [your_choice,computer_choice] in win:
                self.your_win_number+=1
                self.current_round+=1
            else:
                self.computer_win+=1
                self.current_round+=1

        if self.your_win_number>self.computer_win:
            print("you win, yours: ",self.your_win_number)
        else:
            print("computer win, yours: ",self.your_win_number)

khanh=Rock_paper_scissors(3)
khanh.action()