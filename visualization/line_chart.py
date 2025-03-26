# A wide tool veriety of tools exist for visulization one of them is matplotlib.
from matplotlib import pyplot as plt

years = [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980]
gdp = [300.2, 543.5, 1090.3, 2900.0, 4001.9, 6000.4, 10000.8, 12000.9 ]

# creating a line chart years on x-axis, gdp on y-axis

plt.plot(years,gdp, color="green", marker="o", linestyle="solid")

# add title
plt.title("Normal Gdp")

# add label to the y-axis
plt.ylabel("Million of Rs")
plt.savefig("Normal_GDP.jpeg")
plt.show()
