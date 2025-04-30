#imports used (including reusing data from linear fit part)
import matplotlib.pyplot as plt
import numpy as np
import math
from linearFit import getCountryData, getHdi, getLife

countries = getCountryData()
hdi = getHdi()
life_expectancy = getLife()
n = len(countries)

#variables set up (I.D.1 and I.D.3)
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

#calculations for c and d from ce^dx (I.D.1)
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
print("wBar, C, D:", wBar, c, d)

#calculations for I.D.3
for country in countries:
    x_i = country[0]
    y_i = country[1]
    ssre += (y_i - c * math.e ** (d * x_i)) * (y_i - c * math.e ** (d * x_i))
    syy += (y_i - yBar) * (y_i - yBar)
r_e_2 = 1 - ssre / syy
print("ssre, syy, r_e_2:", ssre, syy, r_e_2)

#points and exponential regrssion for I.D.2
x = np.linspace(0, 1)
y = c * math.e ** (d * x)
x1 = 0.35
y1 = c * math.e ** (d * x1)
x2 = 0.95
y2 = c * math.e ** (d * x2)

#plotting scatter plot with regression, I.D.2
plt.figure(figsize=(6,8))
plt.xticks(np.arange(0.3, 1.1, 0.1))
plt.xlim(0.3, 1.0)
plt.yticks(np.arange(50, 90, 5))
plt.ylim(50, 90)
plt.scatter(hdi, life_expectancy)
plt.plot(x, y, color="red")
plt.plot(x1, y1, color="red", marker='o')
plt.plot(x2, y2, color="red", marker='o')
plt.annotate(str(x1) + ", " + str(y1), xy=(x1, y1))
plt.annotate(str(x2) + ", " + str(y2), xy=(x2, y2))
plt.title("Life Expectancy vs. HDI, 2022")
plt.xlabel("HDI")
plt.ylabel("Life Expectancy (Years)")
plt.savefig("LinearFit.png")
plt.savefig("ProcessedData/Part3/ExponentialFit.png")