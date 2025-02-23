#imports for plotting and math tools
import matplotlib.pyplot as plt
import numpy as np
import csv

# for life expectancy vs. hdi dataset

#opens dataset and makes it usable, splitting the file line by line
with open("hdr_general.csv", 'r') as f:
    content = f.read()

rows = content.split("\n")

countries = []

for i in range(len(rows)):
    countries.append(rows[i])

#removes description row and blank row at end
countries = countries[1: len(countries) - 1]

#creates hdi and life expectancy values
hdi = []
life_expectancy = []

for x in countries:
    country = x.split(",")
    #filters out data that isn't from 2022
    if country[6] == "2022":
        #only takes valid hdi and life expectancy data
        if country[7] != "NA" and country[8] != "NA":
            hdi.append(float(country[7]))
            life_expectancy.append(float(country[8]))

#plots scatter plot with hdi and life expectancy data
#customizes plot size, tick marks, where plot starts and ends, labels, and titles
#exports plot to another file called HDI_LifeExpectancy.png
plt.figure(figsize=(6,8))
plt.xticks(np.arange(0.3, 1.1, 0.1))
plt.xlim(0.3, 1.0)
plt.yticks(np.arange(50, 90, 5))
plt.ylim(50, 90)
plt.scatter(hdi, life_expectancy)
plt.title("Life Expectancy vs. HDI, 2022")
plt.xlabel("HDI")
plt.ylabel("Life Expectancy (Years)")
plt.savefig("HDI_LifeExpectancy.png")

xy_table = [["X", "Y"]]

for i in range(len(hdi)):
    xy_table.append([hdi[i], life_expectancy[i]])

with open("HDI_LifeExpectancy.csv", 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(xy_table)