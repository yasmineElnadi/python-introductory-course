#3.5 try
def sumOfOddPlace(n):
    sumOdd = 0
    c = 1
    while n != 0:
        x = n % 10
        n = n // 10
        if c % 2 != 0:
            sumOdd += x
        c += 1
    return sumOdd


def getDigit(n):
    if (n >= 0) and (n <= 9):
        z = n
    else:
        z = n % 10 + n // 10
    return z

def sumOfDoubleEvenPlace(n):
    sumEven = 0
    c = 1
    while n != 0:
        x = n % 10
        n = n // 10
        if c % 2 == 0:
            x = x * 2
            x = getDigit(x)
            sumEven += x
        c += 1
    return sumEven


def isValid(n):
    x = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    if x % 10 == 0:
        print("the card number is valid")
    else:
        print("the card number is not valid")


number = eval(input("please enter your card number:"))
print(isValid(number))
#print(sumOfDoubleEvenPlace(number))
#print(sumOfOddPlace(number))






















