import matplotlib.pyplot as plot
import numpy as np
import seaborn as sns

sns.set()
data = np.genfromtxt('./dataset/housing.csv',delimiter=',',skip_header=1)

print(data)
print("data info")
print(data.shape)

element = data[:, 0]
target = data[:, 3]

# plot.axis(xmin=0, ymin=0)
plot.xticks(fontsize=10)
plot.yticks(fontsize=10)
plot.xlabel("RM", fontsize=10)
plot.ylabel("MEDV", fontsize=10)

plot.plot(element, target,"bo")
plot.savefig ("/src/images/result.png")

