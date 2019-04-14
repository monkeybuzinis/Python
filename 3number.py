##1
# from random import randint
# for i in range(0,50):
#     x= randint(3,6)
#     print(x)

# #2
# from random import randint
# x=randint(1,50)
# y=randint(2,5)
# print(x,y)
# print(x**y)

# 3
# from random import randint
# x=randint(1,10)
# print(x)
# for i in range(0,x):
#     print("khanh")

# 4
# import random
# print(round(random.uniform(1,10),2))

# 5
# import random
# for i in range (2,51):
#     for j in range(1,i):
#         print(random.randint(1,j))

# 8
# s=eval(input("input number of second: "))
# print(s,"seconds equal",s//60 ,"minutes", s%60 ,"seconds")

# 9
# h=eval(input("enter hour: "))
# a=eval(input("how many hours ahead? "))
# print(((a+h)%24)%12)

# #10
# #a
# power=eval(input('enter the power: '))
# print('the last digit of 2 power to ',power,'is ',2**power%10)

##c
# power=eval(input('enter the power: '))
# digit=eval(input('how many digit? '))
# print('the ',digit, 'digit(s) of 2 power to ',power,'is ',(2**power)%(10**3))

# #13
# import math
# n=eval(input("input a no: "))
# print("sin = ", math.sin(n))

# 19
w = eval(input("width?: "))
h = eval(input("height?: "))
for j in range(0,w*h,w):
    print("")
    for i in range(0+j,w+j,1):
        # override the default setting from \n to a single space
        print(i%10, end=" ")

