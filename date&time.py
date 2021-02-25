import datetime
today =datetime.date.today()
print(today)
birthday = datetime.date(1998, 7, 13)
print(birthday)
days_since_birth =(today - birthday).days
print(days_since_birth)
#datetime.date (Y, N, D )
#datetime.time (h , m, s, ms)
#datetime.datetime (Y, M, D, H, M, s)

