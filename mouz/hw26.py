print("HW26 By Lenny Metlitsky PD9 4/3/2023")

# Write a Python program that creates a list from the user and
# prints the numbers of the list after removing even numbers from it.

def odds_only():
    nums = []
    while True:
        user_input = input("Enter a num or 'done': ")
        if user_input.lower() == "done":
            break
        nums.append(int(user_input))

    new_nums = []
    for num in nums:
        if num % 2 == 1:
            new_nums.append(num)

    print("Odds only: ", new_nums)

odds_only()

# Shift about an index
def shift(l : list, a : int):
    return l[a + 1: ] + l[:a + 1] 

def is_circular_identical(a : list, b : list):
    for i in range(len(a)):
        if shift(a, i) == b:
            return True
        
    return False

def challenge_question():
    print("Challenge Question: ")
    # Write a python program to check whether two lists are circularly identical.

    l1 = [10, 10, 10, 0, 0]
    l2 = [10, 10, 0, 0, 10]
    l3 = [0, 10, 0, 0, 10]

    print("List 1: ", l1)
    print("List 2: ", l2)
    print("List 3: ", l3)

    print("Are l1 and l2 circular-ly identical?", is_circular_identical(l1, l2))
    print("Are l2 and l3 circular-ly identical?", is_circular_identical(l1, l3))

challenge_question()
