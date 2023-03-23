print("HW24 By Lenny Metlitsky PD9 3/23/2023")

# Write a Python function to convert a given string to all uppercase 
# if it contains at least 2 uppercase characters in the first 4 characters.

def convert(s : str):
    upper_count = 0

    for char in s[:min(4, len(s))]:
        if ord(char) >= 65 and ord(char) <= 90: # If it is an upper case A-Z
            upper_count += 1

        if upper_count >= 2:
            # Already has 2 upper case letters
            break

    if upper_count >= 2:
        return s.upper()
    else:
        return s

print("Converted string of 'test'", convert("test") )
print("Converted string of 'TEsting'", convert("TEsting") )

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

print("Inverted string of 'Python': ", invert_string("Python"))
print("Inverted string of 'Exercises': ", invert_string("Exercises"))
