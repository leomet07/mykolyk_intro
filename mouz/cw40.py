from matplotlib import pyplot as plt

y = ["Apple", "Orange", "Banana", "Kiwifruit", "Blueberry", "Grapes"]

x = [35, 30, 10, 25, 40, 5]

colors = ["#ff4141", "#f57900", "#fce94f", "#73d216", "#729fcf", "#5c3566"]

plt.title("Nicest Fruit",fontdict={"family" : "serif", "size" : 22, "weight" : "bold", "style" : "italic"})
plt.xlabel("Number of People",fontdict={"family" : "serif", "size" : 16})

for i in range(len(x)):
    yi = y[i]
    xi = x[i]
    plt.barh(yi, xi, color=colors[i])

plt.show()