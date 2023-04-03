print("CW26 By Lenny Metlitsky PD9 4/3/2023")

# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 20 (both included).
squares = [i ** 2 for i in range(1, 21)]
first_five = squares[: 5]
last_five = squares[14:]

print("Total list: ", squares)
print("First five: ", first_five)
print("Last five: ", last_five)

def do_now():
    print("Do now: Grade calculator")
    grades = []
    while True:
        user_input = input("Enter a grade or 'done': ")
        if user_input.lower() == "done":
            break
        grades.append(float(user_input))


    avg = sum(grades) / len(grades)
    print("Your average is: ", avg)

do_now()