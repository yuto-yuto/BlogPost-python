import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import seaborn as sns

def calculateLoss(X, Y, weight, bias = 0):
    predictedLine = X * weight + bias
    return np.average((predictedLine - Y) ** 2)

def trainWithBias(X, Y):
    weight = 14019946383
    bias = 0
    learningRate = 0.1
    for i in range(1000000):
        currentLoss = calculateLoss(X, Y, weight, bias)
        loss1 = calculateLoss(X, Y, weight + learningRate, bias)
        loss2 = calculateLoss(X, Y, weight - learningRate, bias)
        loss3 = calculateLoss(X, Y, weight, bias + learningRate)
        loss4 = calculateLoss(X, Y, weight, bias - learningRate)

        if i % 200 == 0:
            plot.plot(X, Y, "bo")
            image = plot.plot([0, 10], [0, 10 * weight + bias], linewidth = 1.0, color = "g")
            images.append(image)
            print(i, currentLoss)

        minLoss = min(currentLoss, loss1, loss2, loss3, loss4)
        if minLoss == loss1:
            weight += learningRate
        elif minLoss == loss2:
            weight -= learningRate
        elif minLoss == loss3:
            bias += learningRate
        elif minLoss == loss4:
            bias -= learningRate
        else:
            return (weight, bias)

    return (weight, bias)


figure = plot.figure()
images = []

data = np.genfromtxt('./dataset/housing.csv', delimiter = ',', skip_header = 1)
X = data[:, 0]
Y = data[:, 3]

weight = trainWithBias(X, Y)

sns.set()
plot.xticks(fontsize = 10)
plot.yticks(fontsize = 10)
plot.xlabel("RM", fontsize = 10)
plot.ylabel("MEDV", fontsize = 10)

ani1 = animation.ArtistAnimation(figure, images, interval = 100)
ani1.save("/src/images/regression-with-bias.gif", writer = "imagemagick")

plot.plot(X, Y,"bo")
plot.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
plot.savefig("/src/images/linear-regression-with-bias.png")
