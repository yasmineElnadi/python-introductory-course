#calculate energy
M=float(input("Enter the amount of water in Kilograms:"))
print("the temperature values are in Celsius")
temp1=float(input("Enter the initial temperature:"))
temp2=float(input("Enter the final temperature:"))

Q=M*(temp2-temp1)*4184

print("the energy needed is", format(Q, ".2f"),"joules")
