#12
# for i in range (0,200):
#     if((i%5==2)and(i%6==3)and(i%7==2)):
#         print(i)

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
    print("you WIN :) computer played ",computer)X
else:
    print("you LOSE :( computer played ",computer)