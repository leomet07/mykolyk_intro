from matplotlib import pyplot as plt

y = [9, 26, 32, 24, 10]
colors = ["#8F7AD8", "#2FA4FA", "#30E9A9", "#FEBE44", "#FE687D"]
labels = [str(i) + "%" for i in y]

plt.pie(y, colors = colors,labels=labels, labeldistance=0.7)
plt.show() 

y = [16.53, 13.18, 25.52, 12.47, 8.87, 23.59]
colors = ["#FFD92F", "#A6D854", "#E78AC3", "#8DA0CB", "#FC8D62", "#66C2A5"]
labels = [str(i) + "%" for i in y]

plt.pie(y, colors = colors,labels=labels, labeldistance=0.65)
plt.show() 
