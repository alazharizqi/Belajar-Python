import datetime

# INPUT SECTION
print(10*'=','Age Counter',10*'=')
year = int(input('Enter Year : '))
month = int(input('Enter Month : '))
date = int(input('Enter date : '))

# DISPLAY SECTION
birth_date = datetime.date(year, month, date)
print(f"Your birth date : {birth_date}")

today = datetime.date.today()
# print(f"Today : {today}")

# YEARS OLD SECTION
yo_day = today - birth_date
yo = yo_day.days // 365
print(f"Your age : {yo}")