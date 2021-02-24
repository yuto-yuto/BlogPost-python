import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import seaborn as sns

figure = plot.figure()
images = []


def calculateLoss(element, target, weight, bias = 0):
    predictedLine = element * weight + bias
    return np.sum((predictedLine - target) ** 2)


def train(element, target):
    weight = 0
    learningRate = 100
    for i in range(1000):
        if i % 50 == 0:
            plot.plot(element, target, "bo")
            image = plot.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
            images.append(image)
        currentLoss = calculateLoss(element, target, weight)
        print(currentLoss)
        if currentLoss > calculateLoss(element, target, weight + learningRate):
            weight += learningRate
        elif currentLoss > calculateLoss(element, target, weight - learningRate):
            weight -= learningRate
        else:
            return (weight, images)

    return (weight, images)


def trainWithBias(element, target, images):
    weight = 0
    bias = 0
    learningRate = 100
    for i in range(1000):
        if i % 50 == 0:
            plot.plot(element, target, "bo")
            image = plot.plot([0, 10], [0, 10 * weight + bias], linewidth = 1.0, color = "g")
            images.append(image)
        currentLoss = calculateLoss(element, target, weight)
        print(currentLoss)
        if currentLoss > calculateLoss(element, target, weight + learningRate):
            weight += learningRate
        elif currentLoss > calculateLoss(element, target, weight - learningRate):
            weight -= learningRate
        elif currentLoss > calculateLoss(element, target, weight, bias + learningRate):
            bias += learningRate
        elif currentLoss > calculateLoss(element, target, weight, bias - learningRate):
            bias -= learningRate
        else:
            return weight
    return weight


data = np.genfromtxt('./dataset/housing.csv', delimiter = ',', skip_header = 1)
element = data[:, 0]
target = data[:, 3]

images = []
weight = train(element, target)

sns.set()
plot.xticks(fontsize = 10)
plot.yticks(fontsize = 10)
plot.xlabel("RM", fontsize = 10)
plot.ylabel("MEDV", fontsize = 10)

# images.insert(0, plot.plot(element, target,"bo"))
# plot.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
# plot.savefig("/src/images/linear-regression-100.png")

ani = animation.ArtistAnimation(figure, images, interval = 10)
ani.save("/src/images/regression.gif", writer = "imagemagick")
