import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

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

# getting relative frequency from year data by divinding by number of datapoints
relative_dict = {}

for year in years:
    if year not in relative_dict:
        relative_dict[year] = 1
    else:
        relative_dict[year] += 1

for year in relative_dict:
    relative_dict[year] /= len(years)

# error (e1) calculation using formula given
def error_normal(bin_size):
    normal = norm(mean, std_dev)
    total_error = 0
    for year in range(1989, 2022, bin_size):
        bin_sum = 0
        for n in range(year, year + bin_size):
            if n in relative_dict.keys():
                bin_sum += relative_dict[n]
        total_error += (bin_sum - normal.pdf(year + bin_size / 2)) ** 2
    total_error **= 0.5
    return total_error

print("normal")
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

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)

plt.plot(x, p, 'k', linewidth=2) 
plt.savefig("ProcessedData/Part2/Normal/DiscoveryYearHistogram.png")

