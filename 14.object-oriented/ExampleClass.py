class Person:
    
    def __init__(self, name,  age):
        self.name = name
        self.__age = age
    
    def printAge(self):
        print("age is: ", self.__age)
    
    def printName(self):
        print("name is ", self.name)


ly = Person("Ly", 30)
print(ly.name)
ly.printAge()
