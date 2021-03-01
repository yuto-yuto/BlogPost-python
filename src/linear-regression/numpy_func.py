import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import seaborn as sns

data = np.genfromtxt('./dataset/housing.csv', delimiter = ',', skip_header = 1)
X = data[:, 0]
Y = data[:, 3]
 
X2 = np.vstack([X, np.ones(len(X))]).T
weight, bias = np.linalg.lstsq(X2, Y)[0]

sns.set()
plot.xticks(fontsize = 10)
plot.yticks(fontsize = 10)
plot.xlabel("RM", fontsize = 10)
plot.ylabel("MEDV", fontsize = 10)

plot.plot(X, Y, "bo")
plot.plot([0, 10], [0 + bias, 10 * weight + bias], linewidth = 1.0, color = "g")
plot.savefig("/src/images/linear-regression-by-numpy.png")
