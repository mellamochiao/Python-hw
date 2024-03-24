def is_leap_year(year):                      # check if its leap year
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def zellers_congruence(day, month, year):   # to find the day of the week
    if month <= 2:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    return (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7

def get_month_days(month, year):            # find how many days in a month
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month in {4, 6, 9, 11}:
        return 30
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28

def generate_calendar(month, year):
    print('Sun Mon Tue Wed Thu Fri Sat')
    first_day = zellers_congruence(1, month, year)
    month_days = get_month_days(month, year)
    if first_day == 0:
        print('    '* 6, end="")
    else:
        print('    '* (first_day - 1), end="")
    day = 1
    while day <= month_days:
        if first_day == 0:
            print(f"{day:2}", end="  ")
            if (first_day+6 + day) % 7 == 0:
                print()
        else:
            print(f"{day:2}", end="  ")
            if (first_day + day-1) % 7 == 0:
                print()
        day += 1
    if (first_day + day) % 7 != 0:
        print()  # 最後一行結束換行
    return ''

try:
    y = int(input("Please input year: "))
    m = int(input("Please input month: "))
    print(generate_calendar(m, y))
except ValueError:
    print("Please enter a valid integer.")
