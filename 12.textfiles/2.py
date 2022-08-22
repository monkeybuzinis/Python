"""
You are given a file called grades.txt, where each line of the file contains a one-word student username and three test scores separated by spaces, like below:.
GWashington 83 77 54
JAdams 86 69 90
"""

lines = [line.strip() for line in open('grades.txt')]
score = [line.split(' ') for line in lines]
name=[]

for i in score:
    for j in range (1,4):
        if int(i[j])<80:
            name+=[i[0]]
            break
        
if name==[0]:
    print('everyone has passed all the tests')
elif len(name)==1:
    print(name[0], 'couldn\'t pass all the tests')
else:
    print(', '.join(name),'couldn\'t pass all tests')

            
