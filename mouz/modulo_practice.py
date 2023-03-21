import random
def getRandomNum():
    return random.randint(-20, 20)

while True:
    a = getRandomNum()
    b = getRandomNum()

    user_input = (input(f"{a} % {b} = ?: "))
    if user_input.lower() == "q":
        break

    num = int(user_input)
    if num == (a % b):
        print("Correct! ")
    else:
        print(f"Incorrect, the answer was {a % b}")
    