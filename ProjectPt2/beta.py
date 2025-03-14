import numpy as np
from scipy.stats import betabinom, expon, lognorm, skewnorm, weibull_max, beta
import matplotlib.pyplot as plt
import math
import normal

years = normal.years
mu = normal.mean

sum = 0
sum_squared = 0
mu = 0
sigma = 0

n = len(years)

for year in years:
    sum += year
    sum_squared += year ** 2
    mu += math.log(year)

mu /= len(years)
sigma = ((n * sum_squared - sum ** 2) / (n * (n - 1))) ** 0.5

relative_dict = normal.relative_dict
a, b, loc, scale = beta.fit(years)

# error calculation using formula given
beta_dist = beta(a, b, loc=loc, scale=scale)

def error_beta(bin_size):
    total_error = 0
    for year in range(1989, 2022, bin_size):
        bin_sum = 0
        for n in range(year, year + bin_size):
            if n in relative_dict.keys():
                bin_sum += relative_dict[n]
        total_error += (bin_sum - beta_dist.pdf(year + bin_size / 2)) ** 2
    total_error **= 0.5
    return total_error

print("beta")
print("bin size 1 error: " + str(error_beta(1)))
print("bin size 2 error: " + str(error_beta(2)))
print("bin size 3 error: " + str(error_beta(3)))
print("bin size 7 error: " + str(error_beta(7)))

# getting the values to plot on the histogram
values = normal.values

x25 = int(values["quartile1"])
x50 = int(values["median"])
x75 = int(values["quartile3"])
mean = float(values["mean"])
std_dev = float(values["variance"]) ** 0.5

# values of a and b from xbar (mean) and s
bound_a = mean - 2 * std_dev
bound_b = mean + 2 * std_dev

# probability of a
p_a = beta_dist.cdf(bound_b) - beta_dist.cdf(bound_a)

# probability of b
p_b = 1 - beta_dist.cdf(x75)

print("p(a) and p(b)")
print(p_a, p_b)

# probability of a and b
p_ab = p_a + p_b - (1 - beta_dist.cdf(bound_a))

print("p(a and b)")
print(p_ab)

# conditional probability of a given b from previous calculations
p_a_given_b = p_ab / p_b
print("p(a given b)")
print(p_a_given_b)

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

# testing lognormal distribution (somehow same as normal distribution?)
# s, loc, scale = lognorm.fit(years)
# p = lognorm.pdf(x, s, loc=loc, scale=scale)

# testing skewed normal distribution
# a, loc, scale = skewnorm.fit(years)
# p = skewnorm.pdf(x, a, loc, scale)

# do not use weibull
# c, loc, scale = weibull_max.fit(years)
# p = weibull_max.pdf(x, c, loc=loc, scale=scale)

# using beta distribution (weird numbers)
p = beta.pdf(x, a, b, loc=loc, scale=scale)

plt.plot(x, p, 'k', linewidth=2)

plt.savefig("ProcessedData/Part2/Other/DiscreteOtherHistogram.png")
