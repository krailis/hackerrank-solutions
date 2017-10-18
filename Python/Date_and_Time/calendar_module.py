import calendar

month, day, year = map(int, input().strip().split())
wd = calendar.weekday(year, month, day)
print(calendar.day_name[wd].upper())
