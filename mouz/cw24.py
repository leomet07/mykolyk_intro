print("CW24 By Lenny Metlitsky PD9 3/23/2023")

# Write a Python program to change a given string to a 
# new string where the first and last chars have been exchanged

def swap(s : str):
    return s[-1] + s[1:len(s) - 1] + s[0] 

def swap_with_loop(s : str):
    store = ""
    i = 0 
    while i < len(s):
        if i == 0:
            store += s[-1]
        elif i == len(s) - 1:
            store += s[0]
        else:
            store += s[i]
        i += 1
    return store

print("Swapping 'plane': " , swap_with_loop("plane"))
print("Swapping 'bird': " , swap_with_loop("bird"))


# Write a Python function to get a string made of 4 copies of the last two 
# characters of a specified string (length must be at least 2).

def insert_end(s : str):
    if len(s) < 2:
        return "ERROR: string not long enough"
    

    return s[len(s) - 2 : ] * 4

def insert_end_with_loop(s : str):
    if len(s) < 2:
        return "ERROR: string not long enough"
        
    last = ""
    i = len(s) - 2

    while i < len(s):
        last += s[i]
        i += 1

    return last * 4

print("4 copies of last 4 chars of 'python': ", insert_end_with_loop("Python"))
print("4 copies of last 4 chars of 'Exercises': ", insert_end_with_loop("Exercises"))