print("CW22 By Lenny Metlitsky PD9 3/15/2023")

# With using a while True
# def sumFromZeroToN(n):
#     running_sum = 0
#     while True:
#         if n < 0:
#             break
#         running_sum += n
#         n -= 1 

#     return running_sum


# Without using a while True 
def sumFromZeroToN(n):
    running_sum = 0
    while n > 0:
        running_sum += n
        n -= 1 

    return running_sum

print(sumFromZeroToN(-3))
print(sumFromZeroToN(4))
print(sumFromZeroToN(10))