#calculate Volume of Cylinder
import math
radius , length= input("please enter the radius and length of a cylinder:").split(",")
radius , length = [float(radius), float(length)]

pi=math.pi
area= radius* radius * pi
volume = area * length 

print ("the area is", format(area, ".2f"), "The volume is", format (volume, ".2f"))
