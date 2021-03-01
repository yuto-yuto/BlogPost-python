import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import seaborn as sns

def calculateLoss(X, Y, weight, bias = 0):
    predictedLine = X * weight + bias
    return np.average((predictedLine - Y) ** 2)

def trainWithBias1(X, Y):
    weight = 0
    bias = 0
    learningRate = 50
    for i in range(20000):
        currentLoss = calculateLoss(X, Y, weight, bias)

        if i % 200 == 0:
            plot.plot(X, Y, "bo")
            image = plot.plot([0, 10], [0 + bias, 10 * weight + bias], linewidth = 1.0, color = "g")
            images1.append(image)
            print(i, weight, bias, currentLoss)

        if currentLoss > calculateLoss(X, Y, weight + learningRate, bias):
            weight += learningRate
        elif currentLoss > calculateLoss(X, Y, weight - learningRate, bias):
            weight -= learningRate
        elif currentLoss > calculateLoss(X, Y, weight, bias + learningRate):
            bias += learningRate
        elif currentLoss > calculateLoss(X, Y, weight, bias - learningRate):
            bias -= learningRate
        else:
            return (weight, bias)

    return (weight, bias)


def trainWithBias2(X, Y):
    weight = 0
    bias = 0
    learningRate = 50
    for i in range(20000):
        currentLoss = calculateLoss(X, Y, weight, bias)
        loss1 = calculateLoss(X, Y, weight + learningRate, bias)
        loss2 = calculateLoss(X, Y, weight - learningRate, bias)
        loss3 = calculateLoss(X, Y, weight, bias + learningRate)
        loss4 = calculateLoss(X, Y, weight, bias - learningRate)

        if i % 200 == 0:
            plot.plot(X, Y, "bo")
            image = plot.plot(
                [0, 10], 
                [0 + bias, 10 * weight + bias], 
                linewidth = 1.0, 
                color = "g")
            images2.append(image)
            print(i, weight, bias, currentLoss)

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

def prepareImage():
    sns.set()
    plot.xticks(fontsize = 10)
    plot.yticks(fontsize = 10)
    plot.xlabel("RM", fontsize = 10)
    plot.ylabel("MEDV", fontsize = 10)


images1 = []
images2 = []

data = np.genfromtxt('./dataset/housing.csv', delimiter = ',', skip_header = 1)
X = data[:, 0]
Y = data[:, 3]

print("---------1----------")
prepareImage()
figure1 = plot.figure()
[weight1, bias1] = trainWithBias1(X, Y)


ani1 = animation.ArtistAnimation(figure1, images1, interval = 150)
ani1.save("/src/images/regression-with-bias1.gif", writer = "imagemagick")

plot.plot(X, Y,"bo")
plot.plot([0, 10], [0 + bias1, 10 * weight1 + bias1], linewidth = 1.0, color = "g")
plot.savefig("/src/images/linear-regression-with-bias1.png")

print("---------2----------")
prepareImage()
figure2 = plot.figure()
[weight2, bias2] = trainWithBias2(X, Y)

ani2 = animation.ArtistAnimation(figure2, images2, interval = 150)
ani2.save("/src/images/regression-with-bias2.gif", writer = "imagemagick")

plot.plot(X, Y,"bo")
plot.plot([0, 10], [0 + bias2, 10 * weight2 + bias2], linewidth = 1.0, color = "g")
plot.savefig("/src/images/linear-regression-with-bias2.png")
