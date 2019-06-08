"""
Write a program that asks the user to enter a word. Rearrange all the letters of the word
in alphabetical order and print out the resulting word. For example, abracadabra should
become aaaaabbcdrr
"""

word=input("enter a word: ")
list_word=list(word)
list_word.sort()
word="".join(list_word)
print(word)

#như vậy sort không chỉ sort số mà còn sort được chữ