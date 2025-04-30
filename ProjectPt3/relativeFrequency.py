import matplotlib.pyplot as plt
import numpy as np

#gets data into usable state by reusing from previous parts
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

#sample mean and variance, II.B.1, II.B.2
n = len(discovery_years)
xBar = 0
sx_2 = 0

#calculation for sample mean and variance, II.B.1, II.B.2
for year in discovery_years:
    xBar += year
xBar /= n
for year in discovery_years:
    sx_2 += (year - xBar) * (year - xBar)
sx_2 /= (n - 1)

#II.C.1
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

#II.C.2
years = list(range(1989, 2022))
plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2022)
plt.ylim(0, 0.4)
plt.hist(discovery_years, edgecolor="black", weights=np.ones_like(discovery_years) / len(discovery_years), bins=years+[2022])
plt.annotate("N_W=" + str(n), xy=(1990, 0.35))
plt.annotate("xBar=" + str(xBar), xy=(1990, 0.32))
plt.annotate("S_X^2=" + str(sx_2), xy=(1990, 0.29))
plt.axvline(quartile1, color="red", linestyle="dotted")
plt.text(quartile1-2, 0.3, "x25")
plt.axvline(median, color="green", linestyle="dotted")
plt.text(median, 0.35, "x50")
plt.axvline(quartile3, color="blue", linestyle="dotted")
plt.text(quartile3, 0.32, "x75")
plt.title("Relative Frequency of Number of Exoplanets Discovered Per Year\nData Set X")
plt.xlabel("Discovery Year, x")
plt.ylabel("Frequency of Planets Discovered, R(x)")
plt.savefig("ProcessedData/Part3/RelativeFrequency.png")