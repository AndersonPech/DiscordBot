import datetime

t = datetime.datetime.today()
t = t + datetime.timedelta(days=1)
future = datetime.datetime(t.year, t.month, t.day, 9, 0, 0)
print(future)