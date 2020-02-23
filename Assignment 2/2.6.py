#sum digits in an integer
integer = int(input("please enter a number between 0 and 1000:"))

digitOne=integer%10    
v=integer//10
digitTwo=v//10
digitThree=v%10

Sum=digitOne+digitTwo+digitThree
print("the sum of the digits is:",format(Sum))

