import matplotlib.pyplot as plt
import numpy as np
import math
from linearFit import getCountryData, getHdi, getLife

countries = getCountryData()
hdi = getHdi()
life_expectancy = getLife()
n = len(countries)

a = 0
d = 0

xBar = 0
yBar = 0
wBar = 0

sum1 = 0
sum2 = 0
sum3 = 0

ssre = 0
syy = 0
r_e_2 = 0

for i in range(len(countries)):
    x_i = countries[i][0]
    y_i = countries[i][1]
    w_i = math.log(countries[i][1])
    xBar += x_i
    yBar += y_i
    wBar += w_i

xBar /= n
yBar /= n
wBar /= n

for i in range(len(countries)):
    x_i = countries[i][0]
    w_i = math.log(countries[i][1])
    sum1 += x_i * w_i
    sum2 += x_i
    sum3 += x_i * x_i

d = (sum1 - (wBar * sum2)) / (sum3 - (xBar * sum2))
a = wBar - d * xBar
c = math.e ** a

for country in countries:
    x_i = country[0]
    y_i = country[1]
    ssre += (y_i - c * math.e ** (d * x_i)) * (y_i - c * math.e ** (d * x_i))
    syy += (y_i - yBar) * (y_i - yBar)

r_e_2 = 1 - ssre / syy
print(r_e_2)

x = np.linspace(0, 1)
y = (math.e ** a) * math.e ** (d * x)

plt.figure(figsize=(6,8))
plt.xticks(np.arange(0.3, 1.1, 0.1))
plt.xlim(0.3, 1.0)
plt.yticks(np.arange(50, 90, 5))
plt.ylim(50, 90)
plt.scatter(hdi, life_expectancy)
plt.plot(x, y, color="red")
plt.title("Life Expectancy vs. HDI, 2022")
plt.xlabel("HDI")
plt.ylabel("Life Expectancy (Years)")
plt.savefig("LinearFit.png")
plt.savefig("ProcessedData/Part3/ExponentialFit.png")