score=0
count=0
list_A=[]
while score >=0:
    score=eval(input("enter test score (to stop enter negative number): "))
    if score>=90:
        count+=1
        list_A+=[score]
else:
    if list_A!=[]:
        average=sum(list_A)/count
        print("the A scores: ",list_A)
        print("average: ",average )
    else:
        print("there is no A score")
