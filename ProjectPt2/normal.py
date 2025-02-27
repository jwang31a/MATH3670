import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

with open("ProcessedData/Part1/Histogram/Years.csv") as file:
    content = file.read()

content = content.split("\n")[:-1]

years = []

for row in content:
    row = row.split(",")
    for year in row:
        year = int(year)
        years.append(year)

with open("ProcessedData/Part1/Histogram/values.csv") as file:
    raw_values = file.read()

raw_values = raw_values.split("\n")[:-1]

values = []

for x in raw_values:
    values.append(x.split(","))

values = dict(values)

mean = float(values["mean"])
std_dev = np.sqrt(float(values["variance"]))



#frequency histogram and customization
plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2023)
plt.title("Number of Exoplanets Discovered Per Year, 1989-2021")
plt.xlabel("Discovery Year")
plt.ylabel("Number of Exoplanets")

plt.hist(years, edgecolor="black", bins=33, range=(1989,2022), density=True, alpha=0.5)

xmin, xmax = plt.xlim() #this has to be after the hist for the right range to show up
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)

plt.plot(x, p, 'k', linewidth=2) 

plt.savefig("ProcessedData/Part2/Normal/DiscoveryYearHistogram.png")
