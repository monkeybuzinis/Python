for t in range (3,9):
        print()
        for r in range (0,6): #4,5,6
                if (t-r) in range (0,7):
        
                        print(r,t-r)
a=False      
for h in range (-3,3):
        print()
        count=0
        
        for r in range (0,6):
                if r-h in range (0,7):
                        count+=1
                        if count==6:
                                
                                a=True
                                break
        if a==True:
                
                break
print(r,r-h)

                                
                                        

