def isDivisibleBy(a, b):
    return a % b == 0

def isLeapYear(year : int):
    return (isDivisibleBy(year, 4) and (not isDivisibleBy(year, 100) or isDivisibleBy(year, 400)))

print("HW20 by Lenny Metlitsky PD9 3/8/2023")

def daysInMonth(month : int, year : int):
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
        
    if month < 8:
        if (isDivisibleBy(month, 2)):
            return 30
        else:
            return 31
    else:
        if (isDivisibleBy(month, 2)):
            return 31
        else:
            return 30

print(daysInMonth( 1, 2010),"...should be 31")
print(daysInMonth( 2, 2011),"...should be 28")
print(daysInMonth( 2, 2000),"...should be 29")
print(daysInMonth( 4, 2011),"...should be 30")
print(daysInMonth( 10 ,2011), "...should be 31")
print(daysInMonth( 11, 2011), "...should be 30")
print(daysInMonth( 10 ,2020), "...should be 31")
print(daysInMonth( 11 ,2020), "...should be 30")