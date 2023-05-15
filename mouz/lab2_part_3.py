import os
from pprint import pprint

def get_filepath(group : int):
    # return f"mountains{group}k.txt"
    return "mountains" + str(group) + "k.txt"


filepath = get_filepath(6)

with open(filepath, "r") as file_obj:
    lines = file_obj.readlines()[1:]
    # pprint(lines)

mountain_dict = {}

# Read through every line in the file
for line in lines:
    line = line.strip() # Clean up lines, remove invisible newline char and spaces and ends
    line = line.replace("\t\t", "\t") # Remove back to back tabs
    info = line.split("\t") # Split by tab, which is the delimiter
    # print("This iteration's parsed info:")
    # print(info)
    name = info[0]

    elevation_meter = int(info[1].replace(",", "")) # Make sure it is a value
    elevation_feet = elevation_meter * 3.28
    mountain_dict[name] = [elevation_meter, elevation_feet]

just_names_list = []
for key in mountain_dict:
    just_names_list.append(key)


print("Just the names")
for name in just_names_list:
    print(name)

print("Just the meters")
# Just print height in meters
for name in just_names_list:
    value = mountain_dict[name]
    meters = value[0]
    print("Height in meters: ", meters)

print("Just the feet")
# Just print height in feet
for name in just_names_list:
    value = mountain_dict[name]
    feet = value[1]
    print("Height in feet: ", feet)

print("All togehter")
# Print name, meters, and feet together
for name in just_names_list:
    value = mountain_dict[name]
    meters = value[0]
    feet = value[1]

    print(str(name) + " is " + str(meters) + " meters tall, or " + str(feet) + " feet." )
