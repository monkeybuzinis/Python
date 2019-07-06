"""
Recall that if s is a string, then s.find('a') will find the location of the first a in s. The
problem is that it does not find the location of every a. Write a function called findall that
given a string and a single character, returns a list containing all of the locations of that character in the string. It should return an empty list if there are no occurrences of the character
in the string.
"""
def findall(s,a):    
    i=0
    location=[]
    l=s.find(a)
    while l!=-1 and i<=len(s):
        location+=[l+i]
        i+=l+1
        l=s[i:].find(a)
    print(location)

s=input("string: ")
w=input("word: ")
findall(s,w)

