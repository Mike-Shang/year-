from datetime import datetime
current = datetime.now()
year = int(input("enter your birthyear : "))
month = int(input("enter your birthmonth : "))
day = int(input("enter your birthday : "))
current_year = current.year
current_month = current.month
current_day = current.day


def function():
    i = []
    k = []
    result = 1
    for i in range(year, current_year):
        if i % 4 == 0 and i % 100 != 0:
            result = result + 366
        else:
            result = result + 365
    for k in range(1, current_month):
        if k in [1, 3, 5, 7, 8, 10, 12]:
            result = result + 31
        elif k in [4, 6, 9, 11]:
            result = result + 30
        elif k in [2]:
            if current_year % 4 == 0 and current_year % 100 != 0:
                result = result + 29
            else:
                result = result + 28
    for k in range(1, month):
        if k in [1, 3, 5, 7, 8, 10, 12]:
            result = result - 31
        elif k in [4, 6, 9, 11]:
            result = result - 30
        elif k in [2]:
            if current_year % 4 == 0 and current_year % 100 != 0:
                result = result - 29
            else:
                result = result - 28

    result = result + current_day - day
    print(result)


function()
