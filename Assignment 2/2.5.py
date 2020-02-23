#calculate tips
subtotal, gratuity = input("please enter subtotal and gartuity:").split(  )
subtotal , gratuity = [float(subtotal), float(gratuity)]

gratuity= (subtotal* gratuity) /100
total = subtotal+gratuity

print("The gratuity is", format(gratuity,".2f"),"and the total is", format(total,".2f"))
