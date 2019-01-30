#! /usr/bin/env python

#
# Project Euler
# Problem 19
#
# Joe Antognini
# Thu May  2 20:54:46 EDT 2013
#

months_with_30days = [4, 6, 9, 11]

def is_leapyear(date):
  '''Tests whether the year is a leap year.'''

  year, month, day, weekday = date
  
  if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
      return False
    else:
      return True
  else:
    return False

def inc_day(date):
  '''Increments the date by one day.  The date is a tuple of the form:
    (year, month, day, weekday)'''

  year, month, day, weekday = date
  
  weekday += 1
  weekday %= 7

  if month == 2 and is_leapyear(date):
    lastday = 28
  elif month == 2 and is_leapyear(date):
    lastday = 29
  elif month in months_with_30days:
    lastday = 30
  else:
    lastday = 31

  if day == lastday:
    if month == 12:
      year += 1
      month = 1
    else:
      month += 1

    day = 1
  else:
    day += 1

  return (year, month, day, weekday)

date = (1900, 1, 1, 1)
count = 0

while date[:2] != (2000, 12, 31):
  if date[2] == 1 and date[3] == 0:
    count += 1

  date = inc_day(date)

print count
