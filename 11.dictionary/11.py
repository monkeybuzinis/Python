"""
In Section 6.10 we met the substitution cipher. This cipher replaces every letter with a different
letter. For instance every a might be replaced with an e, every b might be replaced with an a, etc. 
Write a program that asks the user to enter two strings. Then determine if the second
string could be an encoded version of the first one with a substitution cipher. For instance,
CXYZ is not an encoded version of BOOK because O got mapped to two separate letters.
Also, CXXK is not an encoded version of BOOK, because K got mapped to itself. On the other
hand, CXXZ would be an encoding of BOOK. This problem can be done with or without a
dictionary
"""
store1={}
store2={}

string1=input("enter the first string: ")
string2=input("enter the second string: ")

if len(string1)!=len(string2):
    print("the second string could NOT be an encoded version of the first string")
else:
    list1=list(string1)
    list2=list(string2)

    for i in range (len(string1)):
        if list1[i] in store1:
            store1[list1[i]]=store1[list1[i]]+str(i)
        else:
            store1[list1[i]]=str(i)

    for i in range (len(string2)):
        if list2[i] in store2:
            store2[list2[i]]=store2[list2[i]]+str(i)
        else:
            store2[list2[i]]=str(i)

    if len(store1)!=len(store2):
        print("the second string could NOT be an encoded version of the first string")
    else:
        list_store1=list(store1)
        list_store2=list(store2)

        count=0

        for i in range (len(store1)):
            if list_store1[i]!=list_store2[i] and store1[list_store1[i]]==store2[list_store2[i]]:
                count+=1
                
        if count==len(store1):
            print("the second string COULD BE an encoded of the first one")
        else:
            print("the second string could NOT be an encoded version of the first string")
