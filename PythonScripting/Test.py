import datetime;

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    leapYear=0
    if(year%4 ==0):
    	if(year%100!=0):
            leapYear=1
    elif(year%400==0):
            leapYear=1



    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
    	return 31
    elif(month == 4 or month == 6 or month == 9 or month == 11):
    	return 30
    elif(leapYear == 0 and month == 2):
    	return 28
    elif(leapYear == 1 and month == 2):
    	return 29
    else:
        print("Please Enter a valid month and Year");


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
    if(year >= datetime.MINYEAR and year <=datetime.MAXYEAR):
        print(year);
        if(month>=1 and month<=12):
            num_of_days=days_in_month(year,month)
            if(day>=1 and day<=num_of_days):
                return True;

    return False;



print(is_valid_date(0,1,1));
