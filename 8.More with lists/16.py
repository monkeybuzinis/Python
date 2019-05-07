l=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

gap=[]
for i in range (1,len(l)):
    gap+=[l[i]-l[i-1]]

print(gap)

gap.sort()

print("the maximum gap size: ",gap[-1])

print("the percentage of gap that have size 2: ",round(gap.count(2)*100/len(gap),2),"%") #round() 
