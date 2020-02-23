#number of Years and days
minutes=eval(input("please enter the number of minutes:"))

years = int(minutes/525600)
rem= minutes%525600
days=int(rem/1440)

print(format(minutes),"minuets is approximately",format(years),"years and", format(days),"days")

