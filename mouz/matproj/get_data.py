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
from matplotlib.widgets import Button

def conv_to_float(s: str):
	return float(s.replace(",", ""))

def deaths_100k_only(event):
	plt.close()

	labels = ["United States", "Overall mean (without United States)"]
	data = [conv_to_float(country_data[label]["deaths_100k_2019"]) for label in labels]
	print(labels, data)
	barlist = plt.bar(labels, data)
	barlist[0].set_color("#710004")
	barlist[1].set_color("#050056")
	plt.title("Deaths per 100k people in 2019")
	plt.ylabel("Deaths per 100k people")
	plt.show()


def pie_chart_of_total_deaths():
	nums = []
	labels = []

	for key in country_data:
		if "with" in key:
			continue
		deaths = float(country_data[key]["death_2019"].replace(",", ""))
		labels.append(key)
		nums.append(deaths)

	fig, ax = plt.subplots()

	plt.pie(nums, labels=labels)
	axnext = fig.add_axes([0.81, 0.05, 0.15, 0.075])
	bnext = Button(axnext, 'Deaths out of 100k')
	bnext.on_clicked(deaths_100k_only)
	plt.show()


# plt.gcf().set_size_inches(20,20) #see the magic xoxo, Suhana
# plt.legend(labels, loc="center left")
# Lenny

pie_chart_of_total_deaths()




# binding_id = plt.connect('motion_notify_event', on_move)
# plt.connect('button_press_event', on_click)



# bprev = Button(axprev, 'Previous')
# bprev.on_clicked(callback.prev)

