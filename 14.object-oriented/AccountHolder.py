class AccountHolder:

    def __init__(self, name, id,internetBanking ):
        self.__name = name
        self.__id = id
        self.__balance = 0
        self.__accountNumber = "zjkzjkldsjlkjasdlkjasdlkj"
        self.__internetBanking=internetBanking

    def getName(self):
        return self.__name
    def getID(self):
        return self.__id
    def getBalance(self):
        return self.__balance
    def getAccountNumber(self):
        return self.__accountNumber
    def __nofityUser(self):
        if self.__internetBanking:
            print("Your blance is: ",self.__balance)
    def deleteIB(self):
        self.__internetBanking=False
        return self.__internetBanking

    def registerIB(self):
        self.__internetBanking=True
        return self.__internetBanking

    def deposit(self,money_deposit):
        self.__balance+=money_deposit
        self.__nofityUser()
        return self.__balance
    def withdrawn(self,money_withdrawn):
        if self.__balance>=money_withdrawn:
            self.__balance-=money_withdrawn
            self.__nofityUser()
        else:
            print("your balance is not sufficient")
        return self.__balance
        

bim = AccountHolder("Bim", "201577625", True)
print(bim.getName())
