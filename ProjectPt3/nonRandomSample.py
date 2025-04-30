import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, t
import random
import math
import csv
import randomSample

#II.E.1 reuses old data and creates new data set V
discovery_years = randomSample.discovery_years
n = len(discovery_years)
xBar = randomSample.xBar
sx_2 = randomSample.sx_2
vSet = discovery_years[1143:3431]

#calculations for hypothesis testing, assuming known variance II.E.3
n_v = len(vSet)
vBar = 0
for year in vSet:
    vBar += year
vBar /= n_v
print("n_v, vBar:", n_v, vBar)
v = (vBar - xBar) * math.sqrt(len(vSet)) / math.sqrt(sx_2)
p = 2 * (1 - norm.cdf(v, loc=0, scale=1))
print("v, p, p/2:", v, p, p/2)

print("=====UNKNOWN VARIANCE=====")

#calculations for hypothesis testing, unknown variance, II.E.4.b
sv_2 = 0
for year in vSet:
    sv_2 += (year - vBar) * (year - vBar)
sv_2 /= (n_v - 1)
print("sv_2, sv:", sv_2, math.sqrt(sv_2))
v_v = (vBar - xBar) * math.sqrt(2288) / math.sqrt(sv_2)
p_v = 2 * (1 - t.cdf(x=v_v, df=2287))
print("v_v, p_v:", v_v, p_v)

#II.E.2 relative histogram for V
years = list(range(1989, 2022))
plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2022)
plt.ylim(0, 0.8)
plt.hist(vSet, edgecolor="black", weights=np.ones_like(vSet) / len(vSet), bins=years+[2022])
plt.annotate("N_V=" + str(n_v), xy=(1990, 0.35))
plt.title("Relative Frequency Histogram of Exoplanet Discovery Years,\nNon-Random Sample V")
plt.xlabel("Discovery Year, x")
plt.ylabel("Frequency of Planets Discovered, R(x)")
plt.savefig("ProcessedData/Part3/NonRandomRelativeFrequency.png")