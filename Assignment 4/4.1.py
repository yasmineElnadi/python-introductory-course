class Account:
    def __init__(self, id=0, balance=100, annual_interest_rate=0):
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate =annual_interest_rate

    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id

    def setBalance(self, balance):
        self.__balance = balance
    def getBalance(self):
        return self.__balance

    def setAnnualInterestRate(self, annual_interest_rate):
        self.__annual_interest_rate = annual_interest_rate
    def getAnnualInterestRate(self):
        return self.__annual_interest_rate

    def getMonthlyInterestRate(self):
        return self.__annual_interest_rate/12
    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("withdrawn amount =", amount)
        else:
            print("the balance Insufficient")

    def deposit(self, amount):
        self.__balance += amount
        print("the amount deposited is ", amount)

    def printAccountDetails(self):
        print("the ID is", self.__id, "the current Balance is", self.__balance,
              "the monthly interest rate is", self.getMonthlyInterestRate(), "and the monthly interest is",
              self.getMonthlyInterest())


bank_account = Account(1122, 20000, 0.45)
bank_account.withdraw(2500)
bank_account.deposit(3000)
bank_account.printAccountDetails()


