#3.3


def squrt(n):
    x0=n/2
    diff=1
    while diff > 0.0001:
            x1 = (x0 + (n/x0))/2
            diff=x0-x1
            x0=x1
    return x1
    
            

n= eval(input("please enter the number to calculate its square root:"))
print('the approximate square root of the number is: %0.4f'% squrt(n))

