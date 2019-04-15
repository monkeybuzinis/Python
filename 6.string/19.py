19
s=input("enter a large integer: ")
if len(s)>4:
    for i in range (len(s)-3,0,-3):   #tính từ len(s)-3 hay len(s)-4?
        s=s[:i]+','+s[i:]
print(s)
