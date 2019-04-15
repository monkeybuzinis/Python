
#14

print(1/0)
value=[12,1/3,1/5280,304.8,30.48,3.048,1/3281]
unit=['inche','yard','mile','millimeter','centimeter','meter','kilometer']
feet=eval(input("enter a length in feet: "))
for j in range (len(unit)):
        print((j+1),".",unit[j])
i=eval(input("enter the no associated with the unit you want to convert into: "))
print(feet,"in foot is",feet*value[i-1],"in",unit[i-1])
