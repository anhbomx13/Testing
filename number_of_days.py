def numberOfDays(year, month):
    leap = 0                        #1
    list = [1, 3, 5, 7, 8, 10, 12]
    if 0 > year or year > 3000:     #2
        return 'Invalid year'       #3
    elif month < 1 or month > 12:   #4
        return 'Invalid month'      #5
    elif year % 400 == 0:           #6
        leap = 1                    #7
    elif year % 100 == 0:           #8
        leap = 0                    #9
    elif year % 4 == 0:             #10
        leap = 1                    #11
    if month == 2:                  #12
        return 28 + leap            #13
    if month in list:               #14
        return 31                   #15
    return 30                       #16


if __name__ == "__main__":
    print(numberOfDays(2999, 2))
    print(2999 % 400)





