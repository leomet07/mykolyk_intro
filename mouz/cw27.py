print("CW27 by Lenny Metlitsky 4/18/23")

# Shift about an index
def shift(l : list, a : int):
    return l[a + 1: ] + l[:a + 1] 

def is_circular_identical(a : list, b : list):
    for i in range(len(a)):
        if shift(a, i) == b:
            return True
        
    return False

# Write a python program to check whether two lists are circularly identical.

l1 = [10, 10, 10, 0, 0]
l2 = [10, 10, 0, 0, 10]
l3 = [0, 10, 0, 0, 10]

print("List 1: ", l1)
print("List 2: ", l2)
print("List 3: ", l3)

print("Are l1 and l2 circular-ly identical?", is_circular_identical(l1, l2))
print("Are l2 and l3 circular-ly identical?", is_circular_identical(l1, l3))