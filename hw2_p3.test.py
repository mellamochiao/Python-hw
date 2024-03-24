# Test if it's leap year
try:
    y = int(input("Enter a year: "))
    if is_leap_year(y):
        print('leap')
    else:
        print('nah')
except ValueError:
    print("Please enter a valid integer.")

# Test if it can find the day of the week
try:
    y = int(input("Enter a year: "))
    m = int(input("Enter a month: "))
    d = int(input("Enter a day: "))
    print(zellers_congruence(d, m, y))
except ValueError:
    print("Please enter a valid integer.")

# Test if it knows how many days in a month
try:
    y = int(input("Enter a year: "))
    m = int(input("Enter a month: "))
    print(get_month_days(m, y))
except ValueError:
    print("Please enter a valid integer.")

# Generate calender
try:
    y = int(input("Please input year: "))
    m = int(input("Please input month: "))
    print(generate_calendar(m, y))
except ValueError:
    print("Please enter a valid integer.")



