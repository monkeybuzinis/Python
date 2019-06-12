"""
Repeatedly ask the user to enter a team name and the how many games the team won and
how many they lost. Store this information in a dictionary where the keys are the team names
and the values are lists of the form [wins, losses].
(a) Using the dictionary created above, allow the user to enter a team name and print out
the team’s winning percentage.
(b) Using the dictionary, create a list whose entries are the number of wins of each team.
(c) Using the dictionary, create a list of all those teams that have winning records
"""
team={}
name=input("team name (enter ""done"" for end):  ")
while name!="done":
    win=eval(input("how many games did the team win? "))
    lose=eval(input("how many games did the team lose? "))
    print()
    team[name]=[win,lose]
    name=input("team name (enter ""done"" for end):  ")

#a
print()
name_ask=input("enter team name you want to look for: ")
if name_ask in team:
    win_percentage=team[name_ask][0]/sum([team[i][0] for i in team])*100 
    print("team ",name_ask, "winning percentage: ",win_percentage,"%")

