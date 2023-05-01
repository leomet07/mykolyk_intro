print("CW30 by Lenny Metlitsky PD9 5/1/2023")

# sum_series(10) 
#Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0). 
def sum_series(n : int):
    return n + (sum_series(n - 2) if n - 2 >= 2 else 0)

print(sum_series(10))
print(sum_series(6))

# Write a Python program to calculate the harmonic sum.
def harmonic_sum(n : int):
    return (1 /n) + (harmonic_sum(n - 1) if n > 1  else 0) 

print(harmonic_sum(7))
print(harmonic_sum(4))

# Write a Python program to calculate the harmonic mean. 
def harmonic_mean(n: int):
    return n / harmonic_sum(n)

print(harmonic_mean(5))

# Fib sequence
def fib(n : int):
    return (fib(n - 1) + fib(n - 2) if n > 1 else 1)

for i in range(10):
    print(f"fib sequence with index {i}: ", fib(i))

# Challenge
# Approximate greatest common divisor
def gcd(n: int):
    return (1 / gcd(n - 1)) + (gcd(n - 1) / 2) if n > 1 else 1

print(gcd(3))