"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    leapyear=0
    if(year%4 ==0):
        if(year%100!=0):
            leapyear=1
    elif(year%400==0):
        leapyear=1



    if(month == 1 or month == 3 or month == 5 or month == 7 or
    month == 8 or month == 10 or month == 12):
        return 31
    elif(month == 4 or month == 6 or month == 9 or month == 11):
        return 30
    elif(leapyear == 0 and month == 2):
        return 28
    elif(leapyear == 1 and month == 2):
        return 29
    else:
        print("Please Enter a valid month and Year")


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """

    if(year>=datetime.MINYEAR and year <=datetime.MAXYEAR):
        if(month>=1 and month<=12):
            num_of_days=days_in_month(year,month)
            if(day>=1 and day<=num_of_days):
                return True

    return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if( is_valid_date(year1,month1,day1)  and  is_valid_date(year2,month2,day2)  ):
        date1 = datetime.date(year1,month1,day1)
        date2 = datetime.date(year2,month2,day2)
        if(date2 > date1):
            datediff= date2-date1
            return datediff.days

    return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    startdate = datetime.date(datetime.date.today().year,
    datetime.date.today().month,datetime.date.today().day)
    birthday = datetime.date(year,month,day)
    if( is_valid_date(year,month,day) and birthday<=datetime.date.today()):
        return (startdate-birthday).days
    return 0
