# generating a list 6x6 characters such that there are exactly two of each character

import string
import random

L=2*random.sample(string.punctuation + string.ascii_letters,6*3) # dùng dấu '+' chứ không dùng 'and' được
random.shuffle(L)
print(L)
print()

matrix=[[L[i+j*6] for i in range (6)] for j in range (6)] # cách dùng L[i+j*6] nhanh hơn

for i in range (6):
    for j in range (6):
        print(matrix[i][j], end=" ")
    print()
