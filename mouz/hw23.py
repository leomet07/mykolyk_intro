print("HW23 By Lenny Metlitsky PD9 3/21/2023")

user_input = input("Enter some text: ")

first_last_upper  = user_input[0].upper() + user_input[1: len(user_input) - 1] + user_input[-1].upper()

print(first_last_upper)

# Challenge
# Write a Python function to convert a given string to all uppercase 
# if it contains at least 2 uppercase characters in the first 4 characters.

upper_count = 0

for char in user_input[:min(4, len(user_input))]:
    if ord(char) >= 65 and ord(char) <= 90: # If it is an upper case A-Z
        upper_count += 1

    if upper_count >= 2:
        # Already has 2 upper case letters
        break

if upper_count >= 2:
    new_user_input = user_input.upper()
    print("BECAME ALL UPPERCASE: ", new_user_input)
else:
    print("Nothing changed: ", user_input)

# Another Challenge
#Write a Python program to swap cases of a given string. 
#Python -> pYTHON 
#Exercises -> eXERCISES
#nUMpY -> NumPy

def invert_string(s : str):
    inverted = ""

    for char in s:
        ascii_code = ord(char)
        if ascii_code >= 65 and ascii_code <= 90:
            inverted += chr(ascii_code + 32)
        elif ascii_code >= 97 and ascii_code <= 122:
            inverted += chr(ascii_code - 32)

    return inverted

print("Inverted string: ", invert_string(user_input))
