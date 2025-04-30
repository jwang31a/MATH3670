#imports used
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import random
import math
import csv

#reuses data from before to get it in a usable state
with open("RawData/all_exoplanets_2021.csv", 'r') as f:
    content = f.read()
rows = content.split("\n")
planets = []
for i in range(len(rows)):
    planets.append(rows[i].split(","))
planets = planets[1:len(planets)]
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

print("xBar, sx_2, n:", xBar, sx_2, n)

median = 0
quartile1 = 0
quartile3 = 0

def find_median(list):
    n = len(list)
    if n % 2 == 0:
        print("avg of n//2 and -1 ")
        return (list[n // 2] + list[n // 2 - 1]) / 2
    else:
        print(n // 2)
        return list[n // 2]
    
middle = len(discovery_years) // 2
median = find_median(discovery_years)
quartile1 = find_median(discovery_years[:middle])
quartile3 = find_median(discovery_years[middle + 1:])
print("q1, median, q3:", quartile1, median, quartile3)

#creates a random sample, if one exists already do not overwrite, II.D.1
def random_sample():
    content = None
    randomSet = []
    try:
        with open("ProcessedData/Part3/RandomSample.csv", 'r') as f:
            content = f.read()
        rows = content.split('\n')
        for row in rows:
            split = row.split(',')
            for s in split:
                if s != '':
                    randomSet.append(int(s))
    except:
        randomSet = random.sample(discovery_years, 40)
        randomSet = sorted(randomSet)
        table_form = []
        for i in range (0, len(randomSet,), 5):
            table_form.append(randomSet[i : i + 5])
        with open("ProcessedData/Part3/RandomSample.csv", 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(table_form)
    return randomSet
randomSample = random_sample()

#II.D.2.a) wBar calculation
wBar = 0
for r in randomSample:
    wBar += r
wBar /= len(randomSample)
print("wBar:", wBar)

#II.D.3.b) hypothesis testing calculations
v = (wBar - xBar) * math.sqrt(len(randomSample)) / math.sqrt(sx_2)
p = 2 * (1 - norm.cdf(v, loc=0, scale=1))
print("v, p, p/2:", v, p, p/2)

#II.D.2, plots histogram of random sample
years = list(range(1989, 2022))
plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2022)
plt.ylim(0, 0.4)
plt.hist(randomSample, edgecolor="black", weights=np.ones_like(randomSample) / len(randomSample), bins=years+[2022])
plt.annotate("N_W=40", xy=(1990, 0.35))
plt.title("Relative Frequency Histogram of Exoplanet Discovery Years,\nRandom Sample W")
plt.xlabel("Discovery Year, x")
plt.ylabel("Frequency of Planets Discovered, R(x)")
plt.savefig("ProcessedData/Part3/RandomRelativeFrequency.png")