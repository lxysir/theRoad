# To count how many days between the birthday and current day
###
# input1: birthday(year1, month1, day1)
# input2: current day(year2, month2, day2)
###
# output days
###
# input program
temp1 = input('input your birthday year:')
temp2 = input('input the month:')
temp3 = input('input the day:')
year1 = int(temp1)
month1 = int(temp2)
day1 = int(temp3)
year2, month2, day2 = 2016, 8, 15
print(year1, month1, day1, year2, month2, day2)


def isLeapYear(year):
    # define this year is a leap year
    if year % 400 == 0:
        return True
    else:
        if year % 4 == 0:
            if year % 100 != 0:
                return True
            else:
                return False
        else:
            return False


def daysInMonth(year, month):
    # 3.define the days in a specific month
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        if month == 1 or month == 3 or month == 5 or month == 7\
                or month == 8 or month == 10 or month == 12:
            return 31
        else:
            if isLeapYear(year):
                return 29
            else:
                return 28


def nextDay(year, month, day):
    # 1.assume a simply algorithm: day by day
    #  def how to get next day
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1


def dayIsBefore(year1, month1, day1, year2, month2, day2):
    # 2.count days between dates assuming 30 days in a month
    # 2.1 def the helper procedure to judge the date, assume current
    #     day is always
    #     after birthday.
    if year2 > year1:
        return True
    else:
        if month2 > month1:
            return True
        else:
            if day2 > day1:
                return True
            else:
                return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    # 2.2 def the days between Dates
    days = 0
    # assert dayIsBefore(year1, month1, day1, year2, month2, day2)
    while dayIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def mytest():
    print(nextDay(1999, 12, 30))
    print(nextDay(1999, 2, 28))
    print(nextDay(2000, 5, 31))
    assert isLeapYear(1999) == False
    assert isLeapYear(2000) == True
    assert isLeapYear(2100) == False
    assert isLeapYear(2008) == True
    assert daysInMonth(1999, 12) == 31
    assert daysInMonth(2000, 2) == 29
    assert daysInMonth(2001, 9) == 30
    assert daysInMonth(2001, 2) == 28
    assert dayIsBefore(1999, 12, 30, 2000, 1, 31) == True
    assert dayIsBefore(2000, 3, 20, 2000, 4, 23) == True
    assert dayIsBefore(2000, 5, 20, 2000, 5, 20) == False
    assert dayIsBefore(2000, 6, 20, 2000, 5, 20) == False
    assert daysBetweenDates(1999, 11, 30, 1999, 12, 30) == 30
    # assert daysBetweenDates(1999, 11, 30, 1998, 11, 30) == 'AssertionError'
    assert daysBetweenDates(2000, 1, 1, 2001, 1, 1) == 366
    assert daysBetweenDates(2008, 2, 1, 2008, 6, 1) == 121
    assert daysBetweenDates(2007, 1, 1, 2008, 12, 31) == 730
    print('mytest is finished')

print('Days from your birthday is:', daysBetweenDates(
    year1, month1, day1, year2, month2, day2))
