19
w = eval(input("width?: "))
h = eval(input("height?: "))
for j in range(0,w*h,w):
    print("")
    for i in range(0+j,w+j,1):
        override the default setting from \n to a single space
        print(i%10, end=" ")

