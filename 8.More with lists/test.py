from random import shuffle
names=['khanh','trang','nga','linh','quynhanh','hang']
shuffle(names)
teams=[]
for i in range (0,len(names),2):
    teams.append([names[i],names[i+1]])
print(teams)