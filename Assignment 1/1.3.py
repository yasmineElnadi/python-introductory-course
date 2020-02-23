#print FUN Pattern
#F pattern


for i in range (5):
    for j in range (7):
        if (j==0 or j==1) or (i==0 or i==2):
            print("F", end="")
        else:
            print(end=" ")
    print(end=" ")
    for j in range (7):
        if ((j==0 or j==6) and i <3) or (i==3 and (j==1 or j==5)) or (i==4 and (j==2 or j==3 or j==4)):
            print("U", end="")
        else:
           print(end=" ")
    print(end=" ")
    for j in range (8):
        if (j==0 or j==1 or j==6 or j==7)or (i==1 and j==2) or (j==3 and i==2) or (i==3 and j==4) or (j==5 and i==4):
            print("N", end="")
        else:
            print(end=" ")
    print()   
print()
