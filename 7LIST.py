# #2
# L=[]
# import random

# for i in range (20):
#     L.append(random.randint(1,100))
# #a
# print(L)
# #b
# print(sum(L)/len(L))
# #c
# L.sort()
# print(L[0],L[-1])
# #d
# count=0
# for i in L:
#     if i%2==0:
#         count+=1
# print(count)

#3
# l=[8,9,10]
# #a
# l[1]=17
# #b
# for i in [4,5,6]:
#     l.append(i)
# #c
# l.remove(l[0])   

# #d
# l.sort()
# #e
# l=l*2
# #f
# l[3]=25
# print(l)

#4
# l=eval(input("insert a list with number from 1 to 12: "))
# for i in range (len(l)):
#     if l[i]>10:
#         l[i]=10
# print(l)


#6
#c
# l=[]
# i=1
# for c in "abcdefghijklmnopqrstuvwxyz":
#     l+=[c*i]
#     i+=1
# print(l)

# #8
# n=eval(input("enter an integer: "))
# l=[]
# for i in range (1,n):
#     if n%i==0:
#         l+=[i]
# print(l)

#9

# r=[]
# from random import randint
# for j in range (10000):
#     r+=[randint(1,6)+randint(1,6)]
# for i in range (2,13):
#     print(i,":", r.count(i)/100,"%")

#10
# l=eval(input())
# s=l[:]
# for i in range (len(l)):
#     s[i]=l[(len(l)-1+i)%len(l)]
# print(s)    

#11
# l=[]
# for i in range (12):
#     l+=[0]*(l.count(1)-1)
#     l+=[1]
# print(l)

# #12
# from random import randint

# l=[]
# l1=[]
# l0=[]

# for i in range (100):
#     l+=[randint(0,1)]
# print(l)
# for i in range (100):
#     if l[i]==1:
#         l1+=[i]
# print(l1)
# for i in range (1,len(l1)):
#     l0+=[l1[i]-l1[i-1]-1]
# l0.sort()
# print(l0)
# print("the longest run of 0 is: ",l0[-1])

#13
# from random import randint
# l=[]
# for i in range (10):
#         l+=[randint(0,5)]
# print(l)
# l.reverse()
# for j in range (len(l)):
#         for i in l:
#                 if l.count(i)>1:
#                         l.remove(i)
# l.reverse()
# print(l)

#14
value=[12,1/3,1/5280,304.8,30.48,3.048,1/3281]
unit=['inche','yard','mile','millimeter','centimeter','meter','kilometer']
feet=eval(input("enter a length in feet: "))
for j in range (len(unit)):
        print((j+1),".",unit[j])
i=eval(input("enter the no associated with the unit you want to convert into: "))
print(feet,"in foot is",feet*value[i-1],"in",unit[i-1])
