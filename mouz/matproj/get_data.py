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







# plt.gcf().set_size_inches(20,20) #see the magic xoxo, Suhana
# plt.legend(labels, loc="center left")
# Lenny

def joke_handle(event):
	print("Joke handle")

class Graphing():
	def __init__(self):
		deaths = []
		labels = []

		for key in country_data:
			if "with" in key:
				continue
			calc_deaths = float(country_data[key]["death_2019"].replace(",", ""))
			labels.append(key)
			deaths.append(calc_deaths)
		self.deaths = deaths
		self.labels = labels

	def pie_chart_of_total_deaths(self, event):
		plt.close()

		plt.pie(self.deaths, labels=self.labels)
		axnext = plt.axes([0.81, 0.05, 0.15, 0.075])
		bnext = Button(axnext, 'Deaths out of 100k')
		bnext.on_clicked(self.deaths_100k_only)
		axnext._button = bnext # Keep a reference to the button in memory so it is not deleted by garbage collector
		plt.show()
	
	def deaths_100k_only(self, event):
		plt.close()

		labels = ["United States", "Overall mean (without United States)"]
		data = [conv_to_float(country_data[label]["deaths_100k_2019"]) for label in labels]

		barlist = plt.bar(labels, data)
		barlist[0].set_color("#710004")
		barlist[1].set_color("#050056")
		plt.title("Deaths per 100k people in 2019")
		plt.ylabel("Deaths per 100k people")

		new_axes = plt.axes([0.81, 0.1, 0.15, 0.075])
		pie_button = Button(new_axes, 'Deaths')
		pie_button.on_clicked(self.pie_chart_of_total_deaths)
		new_axes._button = pie_button # Keep a reference to the button in memory so it is not deleted by garbage collector

		plt.show()

Graph = Graphing()
Graph.pie_chart_of_total_deaths("") # Pass in nothing as the event, doesn't matter
