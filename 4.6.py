class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    def setSpeed(self, speed):
        self.__speed = speed

    def getSpeed(self):
        return self.__speed

    def setRadius(self, radius):
        self.__radius = radius

    def getradius(self):
        return self.__radius

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setOn(self, on):
        self.__on = on

    def getON(self):
        return self.__on

    def __fanOperation(self):
        if self.__on == False:
            return "fan is OFF"
        else:
            return "fan is ON"


    def print(self):
        print("speed is ", self.__speed, "radius is ", self.__radius, "color is ",
              self.__color, self.__fanOperation())


fan_1 = Fan(Fan.FAST, 10, 'Yellow', True)
fan_2 = Fan(Fan.MEDIUM, 5, 'Blue', False)

fan_1.print()
fan_2.print()
