# Exercise create a dictionary

days_months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

month =int(input("Please enter a number 1-12 for a month"))

if month == 2:
    leapyear = input('is it a leap year')
    while True:
        if leapyear =='yes':
            days_months[2] = 29
            break
        elif leapyear =='no':
            days_months[2] = 28
        else:
            leapyear = input("please eneter yes or no:")

if month in days_months:
    print(f'numbers of days from months {month} is {days_months[month]}')
else:
    print(" enter a number from 1-12")
