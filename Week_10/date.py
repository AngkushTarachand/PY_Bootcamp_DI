import datetime

today_date = datetime.date.today()

actual_datetime = datetime.datetime.now()
in_15_hours = actual_datetime + datetime.timedelta(hours=15, minutes=10)

print(f"Today is the {today_date.day}/{today_date.month}")
print(f"In 15 hours and 10 minutes it will be the {in_15_hours.day}/{in_15_hours.month}")