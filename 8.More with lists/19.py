L=[1,2]*4*8

k=0

matrix=[[1 for i in range (8)] for j in range (8)]

for i in range (8):
    for j in range (8):
        matrix[i][j]=L[k]
        k+=1

for i in range (8):
    for j in range (8):
        print(matrix[i][j],end=" ")
    print()

