import calendar
import datetime

this_year = datetime.date.today().year
#
# calendar.calendar(this_year) # 문자열
# print(calendar.calendar(this_year))
#
# calendar.setfirstweekday(6) # sunday를 시작으로.
# print(calendar.calendar(this_year))
#
# print(calendar.month(this_year, 5))
#
# calendar.weekday(this_year, 5, 25)

cal = calendar.Calendar(firstweek=6)

cal.monthdatescalendar(this_year, 6) # datetime.date 방식.
cal.monthdayscalendar(this_year, 6)
cal.monthdays2calendar(this_year, 6)

for date in cal.itermonthdates(this_year, 6): # 202X-06-02
    print(date)

for day in cal.itermonthdays(this_year, 6): # 날짜만 표시.
    print(day)

for day in cal.itermonthdays2(this_year, 6): # (날짜, 요일)
    print(day)

for day in cal.itermonthdays3(this_year, 6): # (연도, 달, 날)
    print(day)

