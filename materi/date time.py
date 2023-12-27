import datetime as dt

# hanya tanggal
tanggal = dt.date.today()
print(tanggal.strftime("Tanggal : %Y-%m-%d"))

# hanya jam
jam = dt.datetime.today()
print(jam.strftime("jam : %H:%M"))

# date dan time default
print(dt.datetime.today())

