import math
class QuadraticEquations:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def geta(self):
        return self.__a

    def getb(self):
        return self.__b

    def getc(self):
        return self.__c

    #def checkDiscriminant(self):
       # if (self.__b)**2 - (4 * self.__a * self.__c) == 0:
            #return "the equation has no roots"

    def getDiscriminant(self):
        return (self.__b)**2 - (4* self.__a * self.__c)

    def getRoot1(self):
        return (-(self.__b) + math.sqrt(self.getDiscriminant()))/ (2 * self.__a)

    def getRoot2(self):
        return (-(self.__b) - math.sqrt(self.getDiscriminant()))/(2 * self.__a)

    def printEquation(self):
        if (self.__b)**2 - (4 * self.__a * self.__c) <= 0:
            print("the equation has no roots")
        else:
            print("the First Root is", self.getRoot1(), "the second root is", self.getRoot2())




equation = QuadraticEquations(5,2,1)
equation.printEquation()

equation = QuadraticEquations(5,6,1)
equation.printEquation()

#print(equation.getRoot1())
#print(equation.getRoot2())