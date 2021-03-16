import datetime

x = datetime.datetime.now()
print(x)

# other


x = datetime.datetime.now()
# year
print(x.year)
# weekday
print(x.strftime("%A"))
# mm/dd/yy
print(x.strftime("%x"))
# time
print(x.strftime("%X"))
# weekday + month + day  +time + year
print(x.strftime("%c"))
# example


x = datetime.datetime(2020, 5, 17)


print(x.strftime("%x"))
# date (mmm/dd/yy)
print(x.strftime("%B"))
# month
print(x.strftime("%m"))
# month as a number
print(x.strftime("%d"))
# day
print(x.strftime("%Y"))
# year
print(x.strftime("%c"))
# Mon Dec 31 17:41:00 2018
