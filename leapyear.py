

def check(x):

    #year = int(input("Enter a year: "))

    year = int(x)
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                #print(year, "is a leap year")
                return True
            else:
                #print(year, "is not a leap year")
                return False
        else:
            #print(year, "is a leap year")
            return True
    else:
        #print(year, "is not a leap year")
        return False



