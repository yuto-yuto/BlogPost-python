import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import seaborn as sns

def calculateLoss(X, Y, weight, bias = 0):
    predictedLine = X * weight + bias
    return np.average((predictedLine - Y) ** 2)

def train(X, Y):
    weight = 0
    learningRate = 100
    for i in range(1000):
        currentLoss = calculateLoss(X, Y, weight)

        if i % 50 == 0:
            plot.plot(X, Y, "bo")
            image = plot.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
            images.append(image)
            print(i, weight, currentLoss)

        if currentLoss > calculateLoss(X, Y, weight + learningRate):
            weight += learningRate
        elif currentLoss > calculateLoss(X, Y, weight - learningRate):
            weight -= learningRate
        else:
            return weight
    return weight

def prepareImage():
    sns.set()
    plot.xticks(fontsize = 10)
    plot.yticks(fontsize = 10)
    plot.xlabel("RM", fontsize = 10)
    plot.ylabel("MEDV", fontsize = 10)

figure = plot.figure()
images = []

data = np.genfromtxt('./dataset/housing.csv', delimiter = ',', skip_header = 1)
X = data[:, 0]
Y = data[:, 3]

weight = train(X, Y)

prepareImage()
ani1 = animation.ArtistAnimation(figure, images, interval = 100)
ani1.save("/src/images/regression.gif", writer = "imagemagick")

plot.clf()
prepareImage()
plot.plot(X, Y, "bo")
plot.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
plot.savefig("/src/images/linear-regression-without-bias.png")
