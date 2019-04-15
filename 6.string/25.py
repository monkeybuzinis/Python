25
s=(input("enter an algebraic expression: "))
v=s
for c in "+-*":
    s=s.replace(c," ")

for j in range (len(v)*2):
    for i in range (len(v)):
        if s[i-1]==")" and s[i]!=" ":
            v=v[:i]+'*'+v[i:]
            s=s[:i]+' '+s[i:]
    print(len(v))
    for i in range (len(v)):      
        elif s[i-1]!=" " and s[i]=='(':
            v=v[:i]+'*'+v[i:]
            s=s[:i]+' '+s[i:]
    print(len(v))
    for i in range (len(v)):    
        elif (s[i-1].isalpha() and (s[i] not in " *)")):
            v=v[:i]+'*'+v[i:]
            s=s[:i]+' '+s[i:]
    print(len(v))
    for i in range (len(v)):   
        elif ((s[i-1] not in " *(") and s[i].isalpha()):
            v=v[:i]+'*'+v[i:]
            s=s[:i]+' '+s[i:]
if v[0]=="*":
    v=v[1:]
for i in range (len(v)+1):
    if s[i]==")" and s[i+1]!=" ":
        v=v[:i+1]+'*'+v[i+1:]
        s=s[:i+1]+' '+s[i+1:]
    
    elif s[i]!=" " and s[i+1]=='(':
        v=v[:i+1]+'*'+v[i+1:]
        s=s[:i+1]+' '+s[i+1:]
        
    elif (s[i].isalpha() and (s[i+1] not in " *)")):
        v=v[:i+1]+'*'+v[i+1:]
        s=s[:i+1]+' '+s[i+1:]
        
    elif ((s[i] not in " *(") and s[i+1].isalpha()):
        v=v[:i+1]+'*'+v[i+1:]
        s=s[:i+1]+' '+s[i+1:]

print(v)