#imports used
import matplotlib.pyplot as plt
import numpy as np
import csv

#I.B
#parsing through raw data to get data set in usable state
with open("RawData/hdr_general.csv", 'r') as f:
    content = f.read()
rows = content.split("\n")
countries = []
for i in range(len(rows)):
    countries.append(rows[i])
countries = countries[1: len(countries) - 1]

#parsing through filtered data to get relevant hdi and life expectancy data
hdi = []
life_expectancy = []
for x in countries:
    country = x.split(",")
    if country[6] == "2022":
        if country[7] != "NA" and country[8] != "NA":
            hdi.append(float(country[7]))
            life_expectancy.append(float(country[8]))

#plots scatter plot
plt.figure(figsize=(6,8))
plt.xticks(np.arange(0.3, 1.1, 0.1))
plt.xlim(0.3, 1.0)
plt.yticks(np.arange(50, 90, 5))
plt.ylim(50, 90)
plt.scatter(hdi, life_expectancy)
plt.title("Life Expectancy vs. HDI, 2022")
plt.xlabel("HDI")
plt.ylabel("Life Expectancy (Years)")
plt.savefig("ProcessedData/Part1/Scatter/HDI_LifeExpectancy.png")

#saves hdi and life expectancy data for later reuse
xy_table = [["X", "Y"]]
for i in range(len(hdi)):
    xy_table.append([hdi[i], life_expectancy[i]])
with open("ProcessedData/Part1/Scatter/HDI_LifeExpectancy.csv", 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(xy_table)