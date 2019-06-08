"""
The number 1961 reads the same upside-down as right-side up. Print out all the numbers
between 1 and 100000 that read the same upside-down as right-side up
"""
upside_down=[1,6,8,9,0]
rightside_up=[1,9,8,6,0]
for i in range (1,100000):
    left=str(i)
    right=str(i)[::-1]
    if len(str(int(left)))==len(str(int(right))):
        count=0
        for j in range (len(left)):
            if int(left[j]) in upside_down and int(right[j]) in upside_down:
                if upside_down.index(int(left[j]))==rightside_up.index(int(right[j])):
                    count+=1
            if count==len(left):
                print(i)
                    
    
