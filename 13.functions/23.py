"""
Write a function that is given a 9 × 9 potentially solved Sudoku and returns True if it is
solved correctly and False if there is a mistake. The Sudoku is correctly solved if there are
no repeated numbers in any row or any column or in any of the nine “blocks.”
"""

#write a function to check 9 number in any row, colunm or block
def check9no(L):
    L1=[i for i in range (1,10)]
    L.sort()
    if L1==L:
        return True
    else:
        return False

def check_sudoku(L):
    #check the number of each no from 1-9, by flattenning two-dimensional list first
    check_total_no=False
    L_flatten=[i for M in L for i in M ] # write in the same order as if writing following line by line
    i=1
    while i <10 and L_flatten.count(i)==9:
        i+=1
    if i==10:
        check_total_no=True

    #check row
    check_row=0
    if check_total_no==True:
        row=0
        while row<9:
            L_row=[]
            for colunm in range (0,9):
                L_row+=[L[row][colunm]]
            if check9no(L_row)==True:
                row+=1
            else:
                row=10
        if row==9:
            check_row=1
    else:
        return False
    
    check_colunm=False   
    if check_row==True:
        colunm=0
        while colunm<9:
            L_colunm=[]
            for row in range (0,9):
                L_colunm+=[L[row][colunm]]
            if check9no(L_colunm)==True:
                colunm+=1
            else:
                colunm=10
        if colunm==9:
            check_colunm=1
    else:
        return False
    
    #check block
    check_block=False
    if check_colunm==True:
 
        i=0
        while i<7:
            j=0
            while j<7:
                L_block=[]
                for row in range (i,i+3):
                    for colunm in range(j,j+3):
                        L_block+=[L[row][colunm]]
                if check9no(L_block)== True:
                    j+=3
                else:
                    j=10
            if j==9:
                i+=3
            else:
                return False
        if i==9:
            check_block=True
        else:
            return False
    else:
        return False

    if check_block==True:
        return True
    else:
        return False

sudoku=[[3,1,6,5,7,8,4,9,2]
,[5,2,9,1,3,4,7,6,8]
,[4,8,7,6,2,9,5,3,1]
,[2,6,3,4,1,5,9,8,7]
,[9,7,4,8,6,3,1,2,5]
,[8,5,1,7,9,2,6,4,3]
,[1,3,8,9,4,7,2,5,6]
,[6,9,2,3,5,1,8,7,4]
,[7,4,5,2,8,6,3,1,9]]

print(check_sudoku(sudoku))



