from random import randint
matrix=[[randint(1,100) for i in range (10)] for j in range (10)]
#a
print(matrix)
#b
matrix[2].sort()  # chú ý form sort của list
print(matrix[2][9])
#c
c5=[matrix[i][5] for i in range (10)]
c5.sort()
print(c5[0])

        
