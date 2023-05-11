# 1. Write a Python procedure to read an entire text file (at least 16 lines).

def read_file(filepath : str):
    with open(filepath, "r") as file_obj:
        return file_obj.read()

# 2. Write a Python procedure to read first n lines of a file; n is user input.

def read_first_lines(filepath : str, nlines: int):
    with open(filepath, "r") as file_obj:
        lines = file_obj.readlines()
        return "\n".join(lines[:nlines])

# 3. Write a Python procedure to read last n lines of a file; n is user input

def read_last_lines(filepath : str, nlines : int):
    with open(filepath, "r") as file_obj:
        lines = file_obj.readlines()
        return "\n".join(lines[len(lines) - nlines:])

# 4. Write a Python procedure to read a file line by line and store it into a list. 
#    (remember Python reads the file as a string try to remember what we 
#      used to turn a string into a list)

def read_lines(filepath : str):
    with open(filepath, "r") as file_obj:
        return file_obj.readlines()

# 5. Write a Python procedure to count the number of lines in a text file. 
def line_count(filepath : str):
    with open(filepath, "r") as file_obj:
        return len(file_obj.readlines())
    
fpath = "test.txt"

print(read_file(fpath))
print(read_first_lines(fpath, 3))
print(read_last_lines(fpath, 3))
print(read_lines(fpath))
print(line_count(fpath))
