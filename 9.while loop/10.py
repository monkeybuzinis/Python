"""Write a program that starts with an 5 × 5 list of zeroes and randomly changes exactly ten of
those zeroes to ones."""


matrix=[[0 for c in range (5)] for r in range (5)]

from random import randint # khi đã import random thì lệnh random.randint không sử dụng được
ch=randint(0,24)
i=0

while i<10:
    if matrix[int(ch/5)][ch%5]==0:
        matrix[int(ch/5)][ch%5]=1
        ch=randint(0,24)
        i+=1
    else:
        ch=randint(0,24)
else:
    for r in range (5):
        for c in range (5):
            print(matrix[r][c],end=' ')
        print()
   
                
""" Chú ý bài này mà viết như sau thì có lúc được lúc không vì

matrix=[[0 for c in range (5)] for r in range (5)]

from random import randint 
ch=randint(0,24)
i=0

while matrix[int(ch/5)][ch%5]!=0 and i<10:
    ch=randint(0,24)   
else:
    if i<10:
        matrix[int(ch/5)][ch%5]=1
        i+=1
    else:
        for r in range (5):
            for c in range (5):
                print(matrix[r][c],end=' ')
            print()

"""