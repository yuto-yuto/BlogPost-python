import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import seaborn as sns

def calculateLoss(element, target, weight, bias = 0):
    predictedLine = element * weight + bias
    return np.average((predictedLine - target) ** 2)

def train(element, target):
    weight = 0
    learningRate = 100
    for i in range(1000):
        if i % 50 == 0:
            plot.plot(element, target, "bo")
            image = plot.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
            images.append(image)
        currentLoss = calculateLoss(element, target, weight)
        print(i, currentLoss)
        if currentLoss > calculateLoss(element, target, weight + learningRate):
            weight += learningRate
        elif currentLoss > calculateLoss(element, target, weight - learningRate):
            weight -= learningRate
        else:
            return weight
    return weight


def gradient(element, target, weight, bias):
    predictedLine = element * weight + bias
    return 2 * np.average(element * (predictedLine - target))


def trainWithBias(element, target):
    weight = 14019946383
    bias = 0
    learningRate = 0.1
    for i in range(1000000):
        if i % 200 == 0:
            plot.plot(element, target, "bo")
            image = plot.plot([0, 10], [0, 10 * weight + bias], linewidth = 1.0, color = "g")
            biasImages.append(image)
        currentLoss = calculateLoss(element, target, weight, bias)
        loss1 = calculateLoss(element, target, weight + learningRate, bias)
        loss2 = calculateLoss(element, target, weight - learningRate, bias)
        loss3 = calculateLoss(element, target, weight, bias + learningRate)
        loss4 = calculateLoss(element, target, weight, bias - learningRate)

        minLoss = min(currentLoss, loss1, loss2, loss3, loss4)
        print(i, currentLoss)
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


data = np.genfromtxt('./dataset/housing.csv', delimiter = ',', skip_header = 1)
element = data[:, 0]
target = data[:, 3]



figure1 = plot.figure(1)
figure2 = plot.figure(2)
figure3 = plot.figure(3)
figure4 = plot.figure(4)
fig1 = figure1.add_subplot(1, 1, 1)
fig2 = figure2.add_subplot(1, 1, 1)
fig3 = figure3.add_subplot(1, 1, 1)
fig4 = figure4.add_subplot(1, 1, 1)
images = []
biasImages = []

weight = train(element, target)
weightWithBias = trainWithBias(element, target)

sns.set()
plot.xticks(fontsize = 10)
plot.yticks(fontsize = 10)
plot.xlabel("RM", fontsize = 10)
plot.ylabel("MEDV", fontsize = 10)


fig1.plot(element, target,"bo")
fig1.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
figure1.savefig("/src/images/linear-regression-without-bias.png")

fig3.plot(element, target,"bo")
fig3.plot([0, 10], [0, 10 * weightWithBias[0] + weightWithBias[1]], linewidth = 1.0, color = "g")
figure3.savefig("/src/images/linear-regression-with-bias.png")

# ani1 = animation.ArtistAnimation(figure2, images, interval = 10)
# ani1.save("/src/images/regression.gif", writer = "imagemagick")

# ani2 = animation.ArtistAnimation(figure4, biasImages, interval = 10)
# ani2.save("/src/images/regression-with-bias.gif", writer = "imagemagick")
