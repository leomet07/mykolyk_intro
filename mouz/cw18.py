# By Lenny Metlitsky PD9 3/7/23

from math import pi, sqrt
def circle_area(radius : int):
    return (radius ** 2) * pi

print("Area of a circle with radius 1:", circle_area(1))
print("Area of a circle with radius 2:", circle_area(2))
print("Area of a circle with radius 3:", circle_area(3))

def tri_area(base : int, height : int):
    return base * height * 0.5

print("Area of a triangle with base 1 and height 1:", tri_area(1, 1))
print("Area of a triangle with base 2 and height 2:", tri_area(2, 2))
print("Area of a triangle with base 3 and height 1:", tri_area(3, 1))


def square_of_sums(x : int, y : int):
    return (x + y) ** 2

print('x= 3, y = 4, expected 49:', square_of_sums(3, 4))
print('x= 2, y = 1, expected 9:', square_of_sums(2, 1))
print('x= 7 y = 2, expected 81:', square_of_sums(7, 2))

def euclid_dist(x1 : int, y1 : int, x2 : int, y2 : int):
    return sqrt(abs(x1 - x2) + abs(y1 - y2))

print("Euclid dist: (1, 1) (2, 2)", euclid_dist(1,1,2,2))
print("Euclid dist: (1, 1) (3, 3)", euclid_dist(1,1,3,3))
print("Euclid dist: (1, 1) (3, 1)", euclid_dist(1,1,3,1))
print("Euclid dist: (1, 1) (6, 18)", euclid_dist(1,1,6,18))


## CHALLENGE QUESTION
# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time. 
def convert_to_24_hour(time : str):
    split_time = time.split(" ")[0].split(":") # Split into hours and everything else
    hours = int(split_time[0])

    am_pm = time.split(" ")[1]
    if am_pm.lower() == "pm":
        hours = hours + 12 

    return str(hours) + ":" + ":".join(split_time[1:])

print('Challenge question, convert "09:06:10 PM" to 24 hour time->> ', convert_to_24_hour("09:06:10 PM"))