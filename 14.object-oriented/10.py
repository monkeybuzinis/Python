class Game_Array:
    def __init__(self):
        self.A=[[0 for c in range (7)] for r in range (6)]
        self.player=1
        self.winner=0
        self.count=0

    def player_turn(self,t_f):
        if t_f==True:
            player_choice=eval(input("it's player "+ str(self.player)+"'s turn, enter your choice: "))
        else:
            player_choice=eval(input("that is already an occupied place, please enter again: "))

        return player_choice

    def current_game(self):
        r,c=self.player_turn(True)
        while self.A[r][c]!=0:
            r,c=self.player_turn(False)

        self.A[r][c]=self.player
        self.player=(self.player%2)+1

    def display(self):
        for row in range (6):
            for colunm in range (7):
                print(self.A[row][colunm],end=" ")
            print()

    def check (self,string):
        if "1111" in string:
            return 1
        elif "2222" in string:
            return 2
        else:
            return False

    def find_winner (self):
        out_loop=False
 
        for subtract in range (-3,3):
            string=""         
            for row in range (0,6):
                if row-subtract in range (0,7):
                    string+=str(self.A[row][row-subtract])
                    if self.check(string)!= 0:
                        out_loop=True
                        break
            if out_loop==True:
                break
        
        if out_loop==False:
            for total in range (3,9):
                string=""        
                for row in range (0,6):
                        if (total-row) in range (0,7):
                            string+=str(self.A[row][total-row])
                            if self.check(string)!=False:
                                out_loop=True
                                break
                if out_loop==True:
                    break
        

        if out_loop==False:
            for row in range (6):
                string=""
                for colunm in range (7):
                    string+=str(self.A[row][colunm])
                    if self.check(string)!=False:
                        out_loop=True
                        break
                if out_loop==True:
                    break

        if out_loop==False:
            for colunm in range (7):
                string=""
                for row in range (6):
                    string+=str(self.A[row][colunm])
                    if self.check(string)!=False:
                        out_loop=True
                        break
                if out_loop==True:
                    break

        if out_loop==True:
            self.winner=self.check(string)


    def check_full(self):
        for row in range (6):
            for colunm in range (7):
                if self.A[row][colunm]!=0:
                    self.count+=1
 
        
    def play(self):
        while self.winner==0 and self.count!=6*7:
            self.display()
            self.current_game() 
            self.find_winner()
            self.check_full()           

        if self.winner==1:
            self.display()
            print("player 1 win")
        elif self.winner==2:
            self.display()
            print("player 2 win")
        else:
            self.display()
            print("noone win")

b=Game_Array()
b.play()
