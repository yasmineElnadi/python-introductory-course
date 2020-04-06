import time

class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
        self.__endTime = 0

    def start(self):
        self.__startTime = time.time()

    def getstarttime(self):
        return self.__startTime

    def stop(self):
        self.__endTime = time.time()

    def getstoptime(self):
        return self.__endTime

    def getElapsedTime(self):
        return (self.__endTime - self.__startTime) * 1000

def doWork():
    for i in range(1, 100000000):
        i = i

x = StopWatch()

x.start()
doWork()
x.stop()
print(x.getstarttime())
print(x.getstoptime())
print(x.getElapsedTime())

