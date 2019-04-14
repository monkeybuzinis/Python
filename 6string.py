
#1
# s=input("enter a string: ")
# #a
# print("total number of characters in the string:",len(s))
# #b
# print(s*10)
# #c
# print(s[0])
# #d
# print(s[:3])
# #e
# print(s[-3:])
# #f
# print(s[-1::-1])
# #g
# print(s[6])

# #2
# s=input("write a sentence: ")
# print(len(s))
# count=0
# for i in range (0,len(s)-1):
#     if(s[i]==" " and s[i+1].isalpha()):
#         count=count+1
# if s[0].isalpha():
#     print("number of words in your sentence: ",count+1)
# else: 
#     print("number of words in your sentence: ",count)
    
# #4
# v="aeuio"
# s=input("enter a string: ")
# a=0
# for i in range(5):
#     if(v[i] in s):
#         a=1
# if(a):
#     print("yes")
# else:
#     print("no")

# #5
# s=s.replace(s[1],"*")
# new_s=s+"!!!"
# print(new_s)       

# #6
# v=",."

# for c in v:
#     s=s.replace(c,"")
# print(s)

#7
# for c in s:
#     if c==" ":
#         s=s.replace(c,"")
# if s==s[::-1]:
#     print("your sentence or word is a palindrome")
# else:
    # print("not")

#9
# n=eval(input("enter the number: "))
# for i in range (n):
#      print(" "*i,i+1)

# #10
# s=input("enter a string: ")
# for c in s:
#     print(c*2)

# #11
# s=input("enter a word containing letter a: ")
# m=s.index('a')
# print(s[:(s.index('a')+1)])
# print(s[(s.index('a')+1):])

#12
# s=input("enter a string: ")
# new=''
# s2=s[1::2].upper()
# i=0
# for c in s2:
#      new+=s[i]+c
#      i+=2
# if len(s)%2==0:
#     print(new)
# else: print(new+s[-1])


# #13
# print("enter 2 strings with same length:")
# s1=input("string 1: ")
# s2=input("string 2: ")
# i=0
# new=''
# if (len(s1)==len(s2)): 
#     for c in s1:
#         new+=c+s2[i]
#         i+=1
#     print(new)
# else:
#     print("you didnt do as what I told")

#14
# s=input("write your name: ")
# new=''
# for i in range (1,len(s)):
#     if(s[i-1]==" " and s[i].isalpha()):
#         new+=s[i].upper()
#     else:
#         new+=s[i]

# if(s[0].isalpha): 
#     print(s[0].upper()+new)
# else:
#     print(new)

# #15
# s='''Do you know how you really are?
# name thinks he is a hero but he is more like a greedy pig! He verbs all day and his belly is adj like that of a pig :)'''
# print("TURN ON YOUR CAPLOCK FIRST ;)")
# name = input("May I know your name please? ")
# verb =input("What will you do when you are hungry? ")
# adj=input("what do you hate more? FAT or THIN? ")
# s=s.replace("name",name)
# s=s.replace("verb",verb)
# s=s.replace("adj",adj)
# print(s)
# input()

#17
# s="abcdefghijklmnopqrstuvwxyz"

# for m in range (26):
#     for j in range (26):
#         print(s[(m+j)%26],end='')
#     print()


#19
# s=input("enter a large integer: ")
# if len(s)>4:
#     for i in range (len(s)-3,0,-3):   #tính từ len(s)-3 hay len(s)-4?
#         s=s[:i]+','+s[i:]
# print(s)

# #21
# # s=input("enter a word: ")
# # import random
# # for i in range (len(s)):
# #     j=random.randint(0,(len(s)-1))
# #     print(s[j],end='')
# #     s=s.replace(s[j],'')
        
#  #22
#  # a
# s=input("enter a string: ")
# v=s[0::2]+s[1::2]
# print(v)
# #b
# i=0
# n=''
# for c in v[:int(len(v)/2)]:
#     if len(v)%2==0:
#         n+=c+v[int(len(v)/2)+i]
#     else:
#         n+=c+v[int(len(v)/2)+1+i]
#     i+=1
# if len(v)%2==0:
#     print(n)
# else: 
#     print(n+v[int(len(v)/2)])
    
#23
#c
# b=eval(input('enter the number: '))
# s=input('enter a string: ')
# v=''
# for i in range (b):
#     v+=s[i::b]
# print("your encrypted message: ",v)
# #d
# n=''
# if len(s)%b==0:
#     for j in range ((int(len(s)/b)+1)):
#         for i in range (b):
#             n+=v[i:len(s):b]
#         v=n
#         n=''
#         print(v)
# else:
#     for j in range ((int(len(s)/b)+2)):
#         for i in range (b):
#             n+=v[i:len(s):b]
#         v=n
#         n=''
#         print(v)

#25
s=(input("enter an algebraic expression: "))
v=s
for c in "+-*":
    s=s.replace(c," ")

for j in range (len(v)*2):
    for i in range (len(v)):
        if s[i-1]==")" and s[i]!=" ":
            v=v[:i]+'*'+v[i:]
            s=s[:i]+' '+s[i:]
    # print(len(v))
    # for i in range (len(v)):      
        elif s[i-1]!=" " and s[i]=='(':
            v=v[:i]+'*'+v[i:]
            s=s[:i]+' '+s[i:]
    # print(len(v))
    # for i in range (len(v)):    
        elif (s[i-1].isalpha() and (s[i] not in " *)")):
            v=v[:i]+'*'+v[i:]
            s=s[:i]+' '+s[i:]
    # print(len(v))
    # for i in range (len(v)):   
        elif ((s[i-1] not in " *(") and s[i].isalpha()):
            v=v[:i]+'*'+v[i:]
            s=s[:i]+' '+s[i:]
if v[0]=="*":
    v=v[1:]
# for i in range (len(v)+1):
#     if s[i]==")" and s[i+1]!=" ":
#         v=v[:i+1]+'*'+v[i+1:]
#         s=s[:i+1]+' '+s[i+1:]
    
#     elif s[i]!=" " and s[i+1]=='(':
#         v=v[:i+1]+'*'+v[i+1:]
#         s=s[:i+1]+' '+s[i+1:]
        
#     elif (s[i].isalpha() and (s[i+1] not in " *)")):
#         v=v[:i+1]+'*'+v[i+1:]
#         s=s[:i+1]+' '+s[i+1:]
        
#     elif ((s[i] not in " *(") and s[i+1].isalpha()):
#         v=v[:i+1]+'*'+v[i+1:]
#         s=s[:i+1]+' '+s[i+1:]

print(v)