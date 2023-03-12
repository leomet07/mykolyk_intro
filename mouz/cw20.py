print("CW20 by Lenny Metlitsky PD9 3/8/2023")

def isDivisibleBy(a, b):
    return a % b == 0

def isLeapYear(year : int):
    return (isDivisibleBy(year, 4) and (not isDivisibleBy(year, 100) or isDivisibleBy(year, 400)))

print("2016:", isLeapYear(2016))
print("2020:", isLeapYear(2020))
print("2021:", isLeapYear(2021))
print("2014:", isLeapYear(2014))
print("2022:", isLeapYear(2022))
print("2024:", isLeapYear(2024))