import matplotlib.pyplot as plt
import numpy as np
import random
import math
import csv

with open("RawData/all_exoplanets_2021.csv", 'r') as f:
    content = f.read()

rows = content.split("\n")
planets = []

#splits data column by column
for i in range(len(rows)):
    planets.append(rows[i].split(","))

#remove description row
planets = planets[1:len(planets)]

#creates discovery year list
discovery_years = []

for i in range(len(planets)):
    discovery_years.append(int(planets[i][6]))

discovery_years = sorted(discovery_years)
n = len(discovery_years)

xBar = 0
sx_2 = 0

for year in discovery_years:
    xBar += year

xBar /= n

for year in discovery_years:
    sx_2 += (year - xBar) * (year - xBar)

sx_2 /= (n - 1)

median = 0
quartile1 = 0
quartile3 = 0

def find_median(list):
    n = len(list)
    if n % 2 == 0:
        return (list[n // 2] + list[n // 2 - 1]) / 2
    else:
        return list[n // 2]
    
middle = len(discovery_years) // 2
median = find_median(discovery_years)
quartile1 = find_median(discovery_years[:middle])
quartile3 = find_median(discovery_years[middle + 1:])

print(quartile1)
print(median)
print(quartile3)

content = None
randomSet = []

try:
    with open("ProcessedData/Part3/RandomSample.csv", 'r') as f:
        content = f.read()
    rows = content.split('\n')
    stringsRandomSet = []
    for row in rows:
        stringsRandomSet.append(row.split(","))
    for r in stringsRandomSet:
        randomSet.append(int(r))
except:
    randomSet = random.sample(discovery_years, 40)
    table_form = []
    for i in range (0, len(randomSet,), 5):
        table_form.append(randomSet[i : i + 5])
    with open("ProcessedData/Part3/RandomSample.csv", 'w') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(table_form)

randomSet = sorted(randomSet)

years = list(range(1989, 2022))

plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2022)
plt.ylim(0, 0.4)
plt.hist(randomSet, edgecolor="black", weights=np.ones_like(randomSet) / len(randomSet), bins=years+[2022])
plt.title("Relative Frequency of Number of Exoplanets Discovered Per Year, Random Sample")
plt.xlabel("Discovery Year, x")
plt.ylabel("Frequency of Planets Discovered, R(x)")
plt.savefig("ProcessedData/Part3/RandomRelativeFrequency.png")