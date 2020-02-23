#wind speed
ta=float(input("Enter the Temperature in Fahrenheit between -58 and 41:"))
v=eval(input("Enter wind speed in miles per hour:"))
if v < 2:
    print("wind speed should be above or equal 2 mph")
else:
    print("the wind chill index is ", format(35.74 + (0.6215*ta) - (35.75* v**0.16) + (0.4275 * ta * v**0.16), ".5f"))
