"""
Write a function called first_diff that is given two strings and returns the first location in
which the strings differ. If the strings are identical, it should return -1.
"""
def first_diff(s1,s2):
    if s1==s2:
        print(-1)
    else:
        i=0
        while (i+1)<=len(s1) and (i+1)<=len(s2) and s1[i]==s2[i]:
            i+=1
    
        else:
            print(i)
s1=input("enter the first string: ")
s2=input("enter the second string: ")
first_diff(s1,s2)