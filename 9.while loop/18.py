matrix=[[0 for i in range (6)] for j in range (6)]
from random import randint
ch=randint(0,36)
time=0
while time<12:
    if matrix[int(ch/6)][ch%6]==0:
        matrix[int(ch/6)][ch%6]=1
        time+=1
        ch=randint(0,36)
    else:
        ch=randint(0,36)
else:
    for i in range (6):
        for j in range (6):
            print(matrix[i][j],end=' ')
        print()
        