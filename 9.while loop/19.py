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
    not_use=[]
    while row<9:
        column=0         
        while column<9:
            not_use=[]           
            for i in range (row):
                not_use+=[matrix[i][column]]
            for j in range (column):
                not_use+=[matrix[row][j]] 

            choice=random.randint(1,9)
            count=0
            if choice in not_use:
                for i in range (1,10):
                    if i in not_use:
                        count+=1
                if count==9:
                    possible=0
                    row=10
                    column=10
                else:
                    while choice in not_use:
                        choice=random.randint(1,9) 
                    else:
                        matrix[row][column]=choice
                        column+=1                       
                        possible+=1
            else:
                matrix[row][column]=choice
                column+=1     
                possible+=1     
        else:
            row+=1

for i in range (9):
    for j in range (9):
        print(matrix[i][j],end=" ")
    print()
print()
print(possible)

        




