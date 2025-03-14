import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import random
import normal

# reusing processed data from normal
years = normal.years
values = normal.values
relative_dict = normal.relative_dict

# getting the values to plot on the histogram
x25 = int(values["quartile1"])
x50 = int(values["median"])
x75 = int(values["quartile3"])
mean = float(values["mean"])
std_dev = float(values["variance"]) ** 0.5

# values of a and b from xbar (mean) and s
bound_a = mean - 2 * std_dev
bound_b = mean + 2 * std_dev

print("a = " + str(bound_a))
print("b = " + str(bound_b))

# probability of a
p_a = 0
for i in range(1989, 2022):
    if bound_a < i and i < bound_b:
        if i in relative_dict.keys():
            p_a += relative_dict[i]

# probability of b
p_b = 0
for i in range(1989, 2022):
    if i > x75:
        if i in relative_dict.keys():
            p_b += relative_dict[i]

print("p(a) and p(b)")
print(p_a, p_b)

# probability of a and b
p_ab = 0
for i in range(1989, 2022):
    if bound_a < i and i < bound_b and i > x75:
        if i in relative_dict.keys():
            p_ab += relative_dict[i]

print("p(a and b)")
print(p_ab)

# conditional probability of a given b from previous calculations
p_a_given_b = p_ab / p_b
print("p(a given b)")
print(p_a_given_b)

# getting random values from above x75
years_above_x75 = [x for x in years if x > x75]
def select_random():
    between_a_b = 0
    for i in range(50):
        trial = random.choice(years_above_x75)
        if bound_a < trial and trial < bound_b:
            between_a_b += 1
    return between_a_b

print("conditional probability = " + str(select_random()))

#frequency histogram, normal distribution overlay, and customization
plt.figure(figsize=(6, 8))
plt.xticks(rotation=90)
plt.hist(years, edgecolor="black", bins=33, range=(1989,2022), density=True, alpha=0.5)
plt.xticks(np.arange(1989, 2023, 1.0))
plt.xlim(1989, 2023)

# dotted lines for x25, x50, and x75
plt.axvline(x25, color="red", linestyle="dotted")
plt.text(x25-2, 0.3, "x25")
plt.axvline(x50, color="red", linestyle="dotted")
plt.text(x50, 0.3, "x50")
plt.axvline(x75, color="red", linestyle="dotted")
plt.text(x75, 0.28, "x75")

#solid lines for mean, +- 2 std devs
plt.axvline(mean, color="blue")
plt.text(mean, 0.2, "x")
plt.axvline(mean - 2 * std_dev, color="blue")
plt.text(mean - 2 * std_dev, 0.2, "a")
plt.axvline(mean + 2 * std_dev, color="blue")
plt.text(mean + 2 * std_dev - 1, 0.2, "b")

plt.title("Number of Exoplanets Discovered Per Year, 1989-2021")
plt.xlabel("Discovery Year, x")
plt.ylabel("Number of Exoplanets, R(x)")
plt.savefig("ProcessedData/Part2/Conditional/ConditionalHistogram.png")