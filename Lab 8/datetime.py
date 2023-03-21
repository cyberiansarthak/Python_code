import datetime
from datetime import date

ct = datetime.datetime.now().timestamp()

days = int(input("Enter number of days: ")) * 24 * 60 * 60

timestamp = date.fromtimestamp(days + ct)
print("Date =", timestamp)
