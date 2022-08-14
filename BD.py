
import datetime as dt

today = dt.date.today()

mydate = dt.date(1989,9,18)
still = mydate - today
print(still.days)

number_of_days = int(input("Enter number of days: "))

years = number_of_days // 365
months = (number_of_days - years *365) // 30
days = (number_of_days - years * 365 - months*30)

print("Years = ", years)
print("Months = ", months)
print("Days = ", days)
