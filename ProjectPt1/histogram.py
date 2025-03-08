#imports for plotting and math tools
import numpy as np
import matplotlib.pyplot as plt
import csv

#for exoplanet dataset

#opens dataset and makes it usable, splitting the file line by line
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
discovery_year = []

for i in range(len(planets)):
    discovery_year.append(int(planets[i][6]))

discovery_year = sorted(discovery_year)

#average calculation
sum = 0

for x in discovery_year:
    sum += x

datapoints = len(discovery_year)

mean = sum / datapoints

#variance calculation
variance = 0

for x in discovery_year:
    variance += x**2

variance -= datapoints * mean**2
variance /= datapoints - 1

#median and quartile 1 and 3 calculations
median = 0
quartile1 = 0
quartile3 = 0

def find_median(list):
    n = len(list)
    if n % 2 == 0:
        return (list[n // 2] + list[n // 2 - 1]) / 2
    else:
        return list[n // 2]
    
middle = len(discovery_year) // 2
median = find_median(discovery_year)
quartile1 = find_median(discovery_year[:middle])
quartile3 = find_median(discovery_year[middle + 1:])

#output for important values
values = [
    ["length", datapoints],
    ["mean", mean],
    ["variance", variance],
    ["median", median],
    ["quartile1", quartile1],
    ["quartile3", quartile3],
]

with open("ProcessedData/Part1/Histogram/values.csv", 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(values)

# print("length: ", datapoints)
# print("mean ", mean)
# print("variance: ", variance)
# print("median: ", median)
# print("quartile 1: ", quartile1)
# print("quartile 3: ", quartile3)

#frequency histogram and customization
plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2022)
plt.hist(discovery_year, edgecolor="black", bins=discovery_year+[2022])
plt.title("Number of Exoplanets Discovered Per Year, 1989-2021")
plt.xlabel("Discovery Year, x")
plt.ylabel("Number of Exoplanets, H(x)")
plt.savefig("ProcessedData/Part1/Histogram/DiscoveryYearHistogram.png")

#relative frequency histogram and customization
plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2022)
plt.ylim(0, 0.4)
plt.hist(discovery_year, edgecolor="black", weights=np.ones_like(discovery_year) / len(discovery_year), bins=discovery_year+[2022])
plt.title("Relative Frequency of Number of Exoplanets Discovered Per Year")
plt.xlabel("Discovery Year, x")
plt.ylabel("Frequency of Planets Discovered, R(x)")
plt.savefig("ProcessedData/Part1/Histogram/RelativeFrequency.png")

table_form = []

for i in range (0, len(discovery_year), 10):
    table_form.append(discovery_year[i : i + 10])

with open("ProcessedData/Part1/Histogram/Years.csv", 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(table_form)