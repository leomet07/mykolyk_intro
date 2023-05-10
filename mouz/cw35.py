# 
# Write a Python procedure to check a dictionary is empty or not

def is_empty(d : dict):
    return len(d.items()) == 0

#Write a Python procedure to find the highest 3 values in a dictionary
def highest_3(d: dict):
    vals = list(d.values())
    vals.sort()
    return vals[-3:]

print("Is empty? {}", is_empty({}))
print("Is empty? {'foo' : 'bar'}", is_empty({"foo" : "bar"}))

v ={'data1':100,'data2':-54,'data3':247, 'data4' : 0}

print("Highest 3: ", highest_3(v))