from matplotlib import pyplot as plt
movies=["dil", "shole","dhadkan", "Gandhi", "Bordar"]
awards=[3,4,5,10,6]

plt.bar(range(len(movies)), awards)

plt.title("My Favourite Movies")
plt.ylabel("# of Academy Awards")

plt.xticks(range(len(movies)), movies)
plt.savefig("bar_chart.jpeg")
plt.show()