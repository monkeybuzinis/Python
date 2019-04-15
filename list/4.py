#4
l=eval(input("insert a list with number from 1 to 12: "))
for i in range (len(l)):
    if l[i]>10:
        l[i]=10
print(l)
