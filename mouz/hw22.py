print("HW22 By Lenny Metlitsky PD9 3/15/2023")

# Recursive method
def sumDigits(n): # Use absolute value to remove the negative sign
    return abs(n) % 10 + (0 if abs(n) < 10 else sumDigits(abs(n) // 10))


print("Sum of the digits of 123:" , sumDigits(123))
print("Sum of the digits of 19:", sumDigits(19))
print("Sum of the digits of -21:", sumDigits(-21))
print("Sum of the digits of -567:", sumDigits(-567))
print("Sum of the digits of 6069:", sumDigits(6069))