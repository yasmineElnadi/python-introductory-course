class stock:
    def __init__(self, symbol, name, previousPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice


    def getStockName(self):
        return self.__name

    def getStockSymbol(self):
        return self.__symbol

    def setStockPreviousPrice(self, previousPrice):
        self.__previousPrice = previousPrice

    def getStockPreviousPrice(self):
        return self.__previousPrice

    def setStockCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getStockCurrentPrice(self):
        return self.__currentPrice

    def getChangePercent(self):
        return ((self.__currentPrice - self.__previousPrice)/self.__previousPrice)*100


today_stock = stock('INTC', 'Intel Corporation', 20.5, 20.35)
print("the price-change percentage is ", today_stock.getChangePercent())
