import math
print("HW21 By Lenny Metlitsky PD9 3/14/2023")

print("Problem 1 inefficient method")
upper_limit = 10000
# Inefficient way to print perfect squares
i = 1
while i <= upper_limit:
    if math.sqrt(i) % 1 == 0:
        # If whole, then is perfect square
        print(i)
    i += 1

print("Problem 1 efficient method")
# More effecient way to print perfect squares
i = 1
while i <= math.floor(math.sqrt(upper_limit)):
    print(i ** 2)
    i += 1


# Problem 2

# Inefficient method
j = 0
running_sum = 0
while j <= 3000:
    if j % 5 == 0:
        running_sum += j
    j += 1
print("Running sum for problem 2 inefficient method:", running_sum)

# Efficient method
j = 0
running_sum = 0
while j <= 3000:
    running_sum += j
    j += 5 # Jump 5 numbers forward at a time, since we start at a multiple of 5
print("Running sum for problem 2 efficient method:", running_sum)

# Problem 3
j = 0
running_sum = 0
while j <= 3000:
    if j % 5 == 0 and j % 7 == 0:
        running_sum += j
    j += 1
print("Running sum for problem 3:", running_sum)
