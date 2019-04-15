
#13
list=['scissors','rock','paper']
import random
computer=random.choice(list)
yourturn=input("let's play: ")
while(yourturn==computer or yourturn not in list):
    #yourturn=input("oops! let's continue: ")
#while(yourturn!=list[0]and yourturn!=list[1]and yourturn!=list[2]):
    yourturn=input("oops! let's continue: ")
if((yourturn==list[0] and computer==list[2]) or (yourturn==list[1] and computer==list[0])or(yourturn==list[2] and computer==list[1])): 
    print("you WIN :) computer played ",computer)
else:
    print("you LOSE :( computer played ",computer)