import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import math

# reusing processed data from part 1: getting list of years
with open("ProcessedData/Part1/Histogram/Years.csv") as file:
    content = file.read()

content = content.split("\n")[:-1]

years = []

for row in content:
    row = row.split(",")
    for year in row:
        year = int(year)
        years.append(year)

# reusing important value data (mean, variance, median, quartile data)
with open("ProcessedData/Part1/Histogram/values.csv") as file:
    raw_values = file.read()

raw_values = raw_values.split("\n")[:-1]

values = []

for x in raw_values:
    values.append(x.split(","))

values = dict(values)

mean = float(values["mean"])
std_dev = np.sqrt(float(values["variance"]))

# print(std_dev)

# getting relative frequency from year data
relative_dict = {}

for year in years:
    if year not in relative_dict:
        relative_dict[year] = 1
    else:
        relative_dict[year] += 1

for year in relative_dict:
    relative_dict[year] /= len(years)

# error calculation using formula given
def error_normal(bin_size):
    sum = 0
    normal = norm(mean, std_dev)
    start = math.floor(1989 + bin_size / 2)
    for year in range(start, 2022, bin_size):
        if year in relative_dict.keys():
            sum += (relative_dict[year] - normal.pdf(year) * bin_size) ** 2
        else:
            sum += (0 - normal.pdf(year) * bin_size) ** 2
    return (sum ** 0.5)

print("bin size 1 error: " + str(error_normal(1)))
print("bin size 2 error: " + str(error_normal(2)))
print("bin size 3 error: " + str(error_normal(3)))
print("bin size 7 error: " + str(error_normal(7)))

#frequency histogram, normal distribution overlay, and customization
plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2023)
plt.title("Number of Exoplanets Discovered Per Year, 1989-2021")
plt.xlabel("Discovery Year, x")
plt.ylabel("Number of Exoplanets, R(x)")

plt.hist(years, edgecolor="black", bins=33, range=(1989,2022), density=True, alpha=0.5)

xmin, xmax = plt.xlim() #this has to be after the hist for the right range to show up
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)

plt.plot(x, p, 'k', linewidth=2) 

plt.savefig("ProcessedData/Part2/Normal/DiscoveryYearHistogram.png")

