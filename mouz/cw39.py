from matplotlib import pyplot as plt

# "Profit graph"
x = list(range(2011, 2020))
y1 = [1550,1750, 2400, 2000, 2250, 3000, 2000, 1500, 2500]
y2 = [1050, 1100, 800, 1250, 1400, 1550, 1000, 500, 1100]

plt.plot(2011, 0)
plt.plot(2011, 3500)
plt.plot (x, y1, color="#e3782d")
plt.plot (x, y2, color="#5795ce")
plt.grid(axis="y")
plt.title("Profit")

plt.show()

x = ["1-5", "6-10", "11-15", "15-20", "20-25"]
y= [10, 8, 6, 11, 5]
plt.bar(x, y, color = "#9bbb59")
plt.title("Bar graph")
plt.xlabel("Number of Books Read")
plt.ylabel("Number of students")
plt.show()