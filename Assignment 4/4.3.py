import time


class Time:
    def __init__(self, currentTime=time.time()):
        currentTime = currentTime % (24 * 3600)
        self.__hour = int(currentTime // 3600)
        currentTime %= 3600
        self.__minute = int(currentTime // 60)
        currentTime %= 60
        self.__second = int(currentTime)

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def getTime(self):
        #return (self.__hour, ":", self.__minute, ":", self.__second)
        return (self.__hour, ':', self.__minute, ":", self.__second)

    def setTime(self, newTime):
        self.__init__(newTime)


t = Time()
print("current Time is:", t.getTime())
newTime = eval(input("enter elapsed time:"))
t.setTime(newTime)
print("The Hour:Minute:Second for Elapsed Time is", t.getTime())

