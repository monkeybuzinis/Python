"""
Write a program that finds all pairs of six-digit palindromic numbers that are less than 20
apart. One such pair is 199991 and 200002.
"""
list_palind=[]
for i in range (100000,1000000):
    if str(i)==str(i)[::-1]:
        list_palind+=[i]
for i in list_palind:
    for j in list_palind:
        if (i-j) in range(1,21):
            print([j,i])
    

    