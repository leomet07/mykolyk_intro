print("CW36 + HW36 by Lenny Metlitsky PD9 5/10/2023")

def get_word_count(s : str):
    words = s.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

userinput = input("Enter some text: ")

print("Word info: ", get_word_count(userinput))

# Write a Python script to generate and print a dictionary that contains
#  a number (between 1 and n) in the form (x, x*x). 

def sqaures_dict(n : int):
    squares = {}
    for i in range(1, n + 1):
        squares[i] = i ** 2
    return squares

print(sqaures_dict(5))

# Write a Python program to drop empty items from a given dictionary.
def drop_empty(d : dict):
    new_dict = {}
    for key in d:
        if d[key] != None:
            new_dict[key] = d[key]
    return new_dict

print("Drop empty: ", drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}))
