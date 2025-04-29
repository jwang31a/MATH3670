import matplotlib.pyplot as plt
import numpy as np
import math

def getCountryData():
    with open("ProcessedData/Part1/Scatter/HDI_LifeExpectancy.csv", 'r') as f:
        content = f.read()
    rows = content.split("\n")[1:-1]
    countries = []
    for i in rows:
        row = i.split(",")
        row = list(map(lambda entry : float(entry), row))
        countries.append(row)
    return countries

countries = getCountryData()
n = len(countries)

a = 0
b = 0

yBar = 0
xBar = 0

bNum = 0
bDen = 0

ssrl = 0
syy = 0

for country in countries:
    x_i = country[0]
    y_i = country[1]
    xBar += x_i
    yBar += y_i

xBar /= n
yBar /= n

for country in countries:
    x_i = country[0]
    y_i = country[1]
    bNum += (x_i - xBar) * (y_i - yBar)
    bDen += (x_i - xBar) * (x_i - xBar)

b = bNum / bDen
a = yBar - b * xBar

for country in countries:
    x_i = country[0]
    y_i = country[1]
    ssrl += (y_i - (a + b * x_i)) * (y_i - (a + b * x_i))
    syy += (y_i - yBar) * (y_i - yBar)
    
r_l_2 = 1 - ssrl / syy

hdi = list(map(lambda row : float(row[0]), countries))
life_expectancy = list(map(lambda row : float(row[1]), countries))

def getHdi():
    return hdi

def getLife():
    return life_expectancy

print("a, b, n:", a, b, n)

x = np.linspace(0, 1)
y = b * x + a

x1 = 0.35
y1 = math.floor((b * x1 + a) * 100) / 100
x2 = 0.95
y2 = math.floor((b * x2 + a) * 100) / 100

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
plt.savefig("ProcessedData/Part3/LinearFit.png")