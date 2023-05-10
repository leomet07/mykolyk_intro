print("HW35 by Lenny Metlitsky PD9 5/10/2023")

def create_dict(a : list, b : list):
    d = {}
    for i in range(min(len(a), len(b))):
        d[a[i]] = b[i]
    return d
x = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
y = [1, 2, 2, 3]

print(create_dict(x, y))
