from bs4 import BeautifulSoup
import requests
from pprint import pprint

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