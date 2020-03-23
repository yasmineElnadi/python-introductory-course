#3.1

def getPentagonalNumber(n):
    pentagonalnumber=int((n*(3*n - 1))/2)
    return pentagonalnumber


for i in range(1, 101):
    print(getPentagonalNumber(i))
