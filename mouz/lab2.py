import math

def get_filepath(group : int):
    # return f"mountains{group}k.txt"
    return "mountains" + str(group) + "k.txt"


def part_1():
    filepath = get_filepath(8)

    with open(filepath, "r") as file_obj:
        lines = file_obj.readlines()[1:]
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

    just_names_list = []
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

def part_2():
    filepath = get_filepath(7)

    with open(filepath, "r") as file_obj:
        lines = file_obj.readlines()[1:]
    mountain_dict = {}

    for line in lines:
        line = line.strip() # Clean up lines, remove invisible newline char and spaces and ends
        line = line.replace("\t\t", "\t") # Remove back to back tabs
        info = line.split("\t") # Split by tab, which is the delimiter

        name = info[0]
        elevation = info[1]
        mountain_dict[name] = elevation

    just_names_list = []
    for key in mountain_dict:
        just_names_list.append(key)

    print("Sorted names:")

    just_names_list.sort()
    for name in just_names_list:
        value = mountain_dict[name]
        # print(f"{key} is {value} meters tall.")
        print(str(name) + " is " + str(value) + " meters tall.")

def part_3():
    filepath = get_filepath(6)

    with open(filepath, "r") as file_obj:
        lines = file_obj.readlines()[1:]

    mountain_dict = {}

    # Read through every line in the file
    for line in lines:
        line = line.strip() # Clean up lines, remove invisible newline char and spaces and ends
        line = line.replace("\t\t", "\t") # Remove back to back tabs
        info = line.split("\t") # Split by tab, which is the delimiter
        name = info[0]

        elevation_meter = int(info[1].replace(",", "")) # Make sure it is a value
        elevation_feet = math.floor(elevation_meter * 3.28)
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

print("\nPart one")
part_1()

print("\nPart two")
part_2()

print("\nPart three")
part_3()