print("HW19 by Lenny Metlitsky PD9 3/8/2023")

def analyze_sound_level():
    sound_level = int(input("Enter a sound level in decibels: "))

    if sound_level > 130:
        print("The sound is louder than a jackhammer.")
    elif sound_level == 130:
        print("The sound is equal to one of a jackhammer.")
    elif 106 < sound_level < 130:
        print("The sound is quieter than a jackhammer but louder than a gas lawnmower")
    elif sound_level == 106:
        print("The sound is equal to one of a gas lawnmower.")
    elif 70 < sound_level < 106:
        print("The sound is quieter than a gas lawnmower but louder than an alarm clock")
    elif sound_level == 70:
        print("The sound is equal to one of an alarm clock.")
    elif 40 < sound_level < 70:
        print("The sound is quieter than an alarm clock but louder than a quiet room")
    elif sound_level == 70:
        print("The sound is equal to one of a quiet room.")
    elif sound_level < 70:
        print("The sound is quieter than a quiet room.")

analyze_sound_level()

def name_that_triangle():
    side1 = input("Enter the length of the first side of a triange: ")
    side2 = input("Enter the length of the second side of a triange: ")
    side3 = input("Enter the length of the third side of a triange: ")

    if side1 == side2 == side3:
        print("All the sides are equal. This is an equilateral triangle.")    
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("Two of the sides are equal. This is an isosceles triangle.")
    else:
        print("No sides are equal. This triangle is scalene.")

name_that_triangle()