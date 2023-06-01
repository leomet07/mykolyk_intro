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

def conv_to_float(s: str):
	if s == "NA":
		return "NA"
	return float(s.replace(",", "").replace("−", "-"))

country_data = {}
for line in data:
	if len(line) < 2:
		continue
	key = line[0]
	if key == "Chile††":
		continue # Chile has broken data
	value = {
		"death_2015" : conv_to_float(line[1]),
		"death_2019" : conv_to_float(line[2]),
		"percent_change" : conv_to_float(line[3]),
		"population_2015" : conv_to_float(line[4]),
		"population_2019" : conv_to_float(line[5]),
		"deaths_100k_2015" : conv_to_float(line[6]),
		"deaths_100k_2019" : conv_to_float(line[7]),
		"deaths_change" : conv_to_float(line[8]),
	}
	country_data[key]=value

pprint(country_data)

# By Sangam

from matplotlib import pyplot as plt
from matplotlib.widgets import Button



class Graphing():
	def __init__(self):
		deaths = []
		labels = []

		for key in country_data:
			if "with" in key:
				continue
			calc_deaths = country_data[key]["death_2019"]
			labels.append(key)
			deaths.append(calc_deaths)
		self.deaths = deaths
		self.labels = labels

	def pie_chart_of_total_deaths(self, event):
		plt.close()
		fig, ax = plt.subplots(figsize=(16, 12), subplot_kw=dict(aspect="equal"))

		title = "Deaths in the richest nations"
		plt.title(title)
		fig.canvas.manager.set_window_title(title)

		wedges, texts = ax.pie(self.deaths)
		axnext = plt.axes([0.81, 0.05, 0.15, 0.075])
		bnext = Button(axnext, 'Deaths out of 100k')
		bnext.on_clicked(self.deaths_100k_only)
		axnext._button = bnext # Keep a reference to the button in memory so it is not deleted by garbage collector

		bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
		kw = dict(arrowprops=dict(arrowstyle="-"),
				bbox=bbox_props, zorder=0, va="center")

		for i, p in enumerate(wedges):
			ang = (p.theta2 - p.theta1)/2. + p.theta1
			y = np.sin(np.deg2rad(ang))
			x = np.cos(np.deg2rad(ang))
			horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
			connectionstyle = f"angle,angleA=0,angleB={ang}"
			kw["arrowprops"].update({"connectionstyle": connectionstyle})
			ax.annotate(self.labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
						horizontalalignment=horizontalalignment, **kw)
		
		

		plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
		plt.show()
	
	def deaths_100k_only(self, event):
		plt.close()
		fig, ax = plt.subplots(figsize=(16, 12))

		labels = ["United States", "Overall mean (without United States)"]
		data = [country_data[label]["deaths_100k_2019"] for label in labels]

		barlist = plt.bar(labels, data)
		barlist[0].set_color("#710004")
		barlist[1].set_color("#050056")

		title = "Deaths per 100k people in 2019"
		plt.title(title)
		fig.canvas.manager.set_window_title(title)

		plt.ylabel("Deaths per 100k people")

		new_axes = plt.axes([0.81, 0.1, 0.15, 0.075])
		pie_button = Button(new_axes, 'Deaths')
		pie_button.on_clicked(self.pie_chart_of_total_deaths)
		new_axes._button = pie_button # Keep a reference to the button in memory so it is not deleted by garbage collector

		plt.subplots_adjust(left=0.3, right=0.7, top=0.9, bottom=0.1)
		plt.show()

Graph = Graphing()
Graph.pie_chart_of_total_deaths("") # Pass in nothing as the event, doesn't matter
