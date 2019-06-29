"""
You are given a file namelist.txt that contains a bunch of names. Print out all the names
in the list in which the vowels a, e, i, o, and u appear in order (with repeats possible). The first
vowel in the name must be a and after the first u, it is okay for there to be other vowels. An
example is Ace Elvin Coulson.
"""

name_list=[line.lower().strip() for line in open ("12.textfiles/namelist.txt")]

for name in name_list:
    index_vowel=[]
    for i in 'aeiou':
        if i in name:
            index_vowel+=[name.index(i)]
   
    sort_index=index_vowel
    sort_index.sort()
 
    if sort_index==index_vowel and len(index_vowel)==5:
        print(name)
