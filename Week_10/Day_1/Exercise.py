import datetime

# from Week_10.date import actual_datetime
#
# today_date = datetime.date.today()
# print(today_date)
#
# in_45_days = actual_datetime + datetime.timedelta(days=45, hours=10, minutes=29, seconds=46)
# print(in_45_days)

string_date = "1/8/2022"

dt = datetime.datetime.now()

in_future = dt + datetime.timedelta(days=45, hours=10, minutes=29, seconds=20)

print(in_future.strftime("%d/%m/%y %H:%M:%S"))

