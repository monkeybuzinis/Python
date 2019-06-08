"""
Write a program to find the smallest positive integer that satisfies the following property: If
you take the leftmost digit and move it all the way to the right, the number thus obtained is
exactly 3.5 times larger than the original number. For instance, if we start with 2958 and move
the 2 all the way to the right, we get 9582, which is roughly 3.2 times the original number.
"""
i=1
new_i=int(str(i)[1:]+str(i)[0])
while new_i/i!=3.5:
    i+=1
    new_i=int(str(i)[1:]+str(i)[0])
else:
    print(i)


