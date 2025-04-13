########################################################################################################
#As we saw already, we can make line charts using plt.plot.
# These are a good choice for showing trends, as illustrated in figure3-6.
########################################################################################################
from matplotlib import pyplot as plt

varience = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x+y for x, y in zip(varience, bias_squared)]
xs = [i for i, _ in enumerate(varience)]

# we can make multiple calls to plt.plot
# to show multiple series on the same report

plt.plot(xs, varience, 'g-', label='variance')              # green solid line
plt.plot(xs, bias_squared, 'r-', label='bias^2')            # red solid line
plt.plot(xs, total_error, 'b:', label='total_error')        # blue solid line

# Because we've assigned labels to each series,
# we can get legend for free (loc=9, means top center)

plt.legend(loc=9)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.savefig("line_charts.jpeg")
plt.show()

