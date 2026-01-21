import datetime # Importing datetime library
import math

"""
stores current date in variable x


"""
x=datetime.datetime.now()

#Display current date

print("Date:", str(x))

print("Year:", x.year)
print("Month:", x.month)
print("Day:", x.day)

print("The date today is:", x.day "/" x.month "/"x.year)

