from bs4 import BeautifulSoup
import requests
from pprint import pprint
import numpy as np
from math import pi

url = "https://www.cdc.gov/mmwr/volumes/71/wr/mm7126a1.htm"
r = requests.get(url)

html_doc = str(r.text)
soup = BeautifulSoup(html_doc, 'html.parser')

# table = soup.table
table = soup.find_all('table')[0]
# print(table)

if "Motor vehicle crash deaths and deaths per 100,000 population" in str(table.caption):
    # print("This is the correct table")
    pass

rows = table.find_all("tr")

data = []
for row in rows:
    row_data = []
    for item in row.find_all("td"):
        row_data.append(item.text)
    if row_data == []:
        continue
    data.append(row_data)

print(data)

# Done by Ushoshi
country_data = {}
for line in data:
    if len(line) < 2:
        continue
    key = line[0]
    value = {
        "death_2015" : line[1],
        "death_2019" : line[2],
        "percent_change" : line[3],
        "population_2015" : line[4],
        "population_2019" : line[5],
        "deaths_100k_2015" : line[6],
        "deaths_100k_2019" : line[7],
        "deaths_change" : line[8],
    }
    country_data[key]=value

pprint(country_data)

# By Sangam

from matplotlib import pyplot as plt
from matplotlib.backend_bases import MouseButton

nums = []
labels = []

for key in country_data:
    if "with" in key:
        continue
    deaths = float(country_data[key]["death_2019"].replace(",", ""))
    labels.append(key)
    nums.append(deaths)

fig, ax = plt.subplots()

# Step 2. Create Annotation Object
annotation = ax.annotate(
    text='',
    xy=(0, 0),
    xytext=(15, 15), # distance from x, y
    textcoords='offset points',
    bbox={'boxstyle': 'round', 'fc': 'w'},
    arrowprops={'arrowstyle': '->'}
)
annotation.set_visible(False)

pie = plt.pie(nums, labels=labels, startangle=90)
# plt.gcf().set_size_inches(20,20) #see the magic xoxo, Suhana
# plt.legend(labels, loc="center left")
# Lenny



def on_move(event):
    if event.inaxes:
        # print(f'data coords {event.xdata} {event.ydata},',
        #       f'pixel coords {event.x} {event.y}')
        pass


def on_click(event):
    print(dir(event))
    y = float(event.ydata)
    x = float(event.xdata)

    slope = y / x
    b = 0
    print(f"y = {slope}x + {0}")

    xforcos = ((1 - ((slope * x + b ) ** 2))) ** 0.5 * -1
    print("X for cos: ", xforcos)

    theta1 = np.arcsin(y) * (180 / pi)
    theta2 = np.arccos(xforcos) * (180 / pi)
    print(theta1, theta2)
    # print(dir(event.canvas))
    if event.button is MouseButton.LEFT:
        annotation_visbility = annotation.get_visible()
        if event.inaxes == ax:
            # print(pie)
            print("Starting to print slices")
            for slice in pie[0]:
                pass
                # print(slice)
                # print("\n\n\n\n\n\n")
                # Now get the angle of where it was clicked
                # Figure out where clicked
                
            print("Ending the print slices")
            # is_contained, annotation_index = pie.contains(event)
            # print(is_contained, annotation_index)
        # print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
        #   ('double' if event.dblclick else 'single', event.button,
        #    event.x, event.y, event.xdata, event.ydata))
        # print('disconnecting callback')
        # plt.disconnect(binding_id)



binding_id = plt.connect('motion_notify_event', on_move)
plt.connect('button_press_event', on_click)

plt.show()
