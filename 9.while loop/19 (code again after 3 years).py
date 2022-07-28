"""
Randomly generate a 9 × 9 list where the entries are integers between 1 and 9 with no repeat
entries in any row or in any column.
"""
import random
L=[i for i in range (1,10)]
possible=0
while possible==0:
    L=random.sample(L,9)
    matrix=[[i for i in L] for j in range (9)]
    row=1
    while row<9:
        colunm=0
        not_use_row=[]
        while colunm<9:

            #add the numbers already in colunm
            not_use_colunm=[]

            for i in range (row+1):
                not_use_colunm+=[matrix[i][colunm]]

            #eliminate the numbers already exist in colunm and row
            can_use=[]
            
            for i in range (1,10):
                if i not in not_use_colunm and i not in not_use_row:
                    can_use+=[i] 
                    
            if can_use !=[] :
                matrix[row][colunm]= random.choice(can_use)
                not_use_row+=[matrix[row][colunm]]
                colunm+=1
                possible+=1
                
            elif can_use==[]:
                possible=0
                row=10
                colunm=10
        else:
            row+=1

for i in range (9):
    for j in range (9):
        print(matrix[i][j],end=" ")
    print()
