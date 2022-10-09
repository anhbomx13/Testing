def numberOfDays(year, month):
    leap = 0
    if 0 > year or year > 3000:
        return 'Invalid year'
    elif month < 1 or month > 12:
        return 'Invalid month'
    elif year % 400 == 0:
        leap = 1
    elif year % 100 == 0:
        leap = 0
    elif year % 4 == 0:
        leap = 1
    if month == 2:
        return 28 + leap
    list = [1, 3, 5, 7, 8, 10, 12]
    if month in list:
        return 31
    return 30


if __name__ == "__main__":
    print(numberOfDays(2999, 2))
    print(2999 % 400)

