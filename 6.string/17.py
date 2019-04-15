#17
s="abcdefghijklmnopqrstuvwxyz"

for m in range (26):
    for j in range (26):
        print(s[(m+j)%26],end='')
    print()
