def numberOfDays(year, month):      #1 def(year, month)
    leap = 0                        #2 def(leap)
    list = [1, 3, 5, 7, 8, 10, 12]  #3 def(list)
    if 0 > year or year > 3000:     #4 p-use(year)
        return 'Invalid year'
    elif month < 1 or month > 12:   #5 p-use(month)
        return 'Invalid month'
    elif year % 400 == 0:           #6 p-use(year)
        leap = 1                    #7 def(leap)
    elif year % 100 == 0:           #8 p-use(year)
        leap = 0                    #9 def(leap)
    elif year % 4 == 0:             #10 p-use(year)
        leap = 1                    #11 def(leap)
    if month == 2:                  #12 p-use(month)
        return 28 + leap            #13 c-use(leap)
    if month in list:               #14 p-use(month, list)
        return 31
    return 30


if __name__ == "__main__":
    print(numberOfDays(2999, 2))
    print(2999 % 400)





