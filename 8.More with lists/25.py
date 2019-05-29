"""  Here is an old puzzle question you can solve with a computer program. There is only one
five-digit number n that is such that every one of the following ten numbers shares exactly
one digit in common in the same position as n. Find n.
01265, 12171, 23257, 34548, 45970, 56236, 67324, 78084, 89872, 99414  """


n=['01265','12171','23257','34548','45970','56236','67324','78084','89872','99414']

matrix=[[0 for j in range (5)] for i in range (10)]

for i in range (10):
    for j in range (5):
        matrix[i][j]=int(n[i][j])

for i in range (10):
        for j in range (5):
                print(matrix[i][j],end=' ')
        print()
print()
r1=0

count=[[0 for c in range (5) ] for r in range (10)]
for r in range (10):
        for c in range (5):
                for rr in range (10):
                        if (r!=rr):
                                if (matrix[rr][c]==matrix[r][c]):
                                        count[r][c]+=1

for r in range (10):
        for c in range (5):
                print(count[r][c],end=' ')
        print()
print()

# find the largest no in matrix count
count_time=0
for r in range (10):
        for c in range (5):
                if count[r][c]!=0:
                        count_time+=1

m=[[0 for c in range (4)] for r in range (count_time)]
i=0
for r in range (10):
        for c in range (5):
                if count[r][c]!=0:
                        m[i][0]=r # row 
                        m[i][1]=c # colunm
                        m[i][2]=matrix[r][c] # value
                        m[i][3]=count[r][c] +1  # time

                        i+=1
for r in range (count_time):
        for c in range (4):
                print(m[r][c],end=' ')
        print()
#tim so lon nhat trong day cuoi
max_colunm=[m[i][4] for i in range (count_time)]
max_colunm.sort()





