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

for line in lines:
    line = line.strip() # Clean up lines, remove invisible newline char and spaces and ends
    line = line.replace("\t\t", "\t") # Remove back to back tabs
    info = line.split("\t") # Split by tab, which is the delimiter
    # print("This iteration's parsed info:")
    # print(info)
    name = info[0]
    elevation = info[1]
    mountain_dict[name] = elevation

# print("Printining the dictionary now...")
# pprint(mountain_dict)

# Just print the names...
# shortcut, not valid for lab :(
# just_names_list = list(mountain_dict.keys())
# print(just_names_list)

just_names_list = []
# for key in list(mountain_dict.keys()):
for key in mountain_dict:
    just_names_list.append(key)

print("Just the names")
for name in just_names_list:
    print(name)

just_values_list = []
for key in mountain_dict:
    value = mountain_dict[key]
    just_values_list.append(value)

print("Just the values:")
for val in just_values_list:
    print(val)

for key in mountain_dict:
    # value = mountain_dict.get(key)
    value = mountain_dict[key]
    just_values_list.append(value)

print("Print the name and height in meters together.")
for name in mountain_dict:
    value = mountain_dict[name]
    # print(f"{key} is {value} meters tall.")
    print(str(name) + " is " + str(value) + " meters tall.")

# Part 2

print("Part two, sorted names")

just_names_list.sort()
for name in just_names_list:
    value = mountain_dict[name]
    # print(f"{key} is {value} meters tall.")
    print(str(name) + " is " + str(value) + " meters tall.")