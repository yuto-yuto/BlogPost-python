import matplotlib.pyplot as plot
import matplotlib.animation as animation
import numpy as np
import seaborn as sns

def getGradient(X, Y, weight, bias = 0):
    weight_loss = X * (X * weight + bias - Y)
    bias_loss = (X * weight + bias - Y)
    weight_gradient = 2 * np.average(weight_loss)
    bias_gradient = 2 * np.average(bias_loss)
    return (weight_gradient, bias_gradient)

def trainByGradientDecent(X, Y):
    weight = 0
    bias = 0
    learningRate = 0.01
    for i in range(20000):
        (weight_gradient, bias_gradient) = getGradient(X, Y, weight, bias)
        weight -= weight_gradient * learningRate
        bias -= bias_gradient * learningRate

        if i % 200 == 0:
            plot.plot(X, Y, "bo")
            image = plot.plot([0, 10], [0 + bias, 10 * weight + bias], linewidth = 1.0, color = "g")
            images.append(image)
            print(i, weight, bias)

        if weight_gradient == 0 and bias_gradient == 0:
            return (weight, bias)

    return (weight, bias)


def prepareImage():
    sns.set()
    plot.xticks(fontsize = 10)
    plot.yticks(fontsize = 10)
    plot.xlabel("RM", fontsize = 10)
    plot.ylabel("MEDV", fontsize = 10)


images = []

data = np.genfromtxt('./dataset/housing.csv', delimiter = ',', skip_header = 1)
X = data[:, 0]
Y = data[:, 3]

print("---------gradient decent----------")
prepareImage()
figure1 = plot.figure()
[weight1, bias1] = trainByGradientDecent(X, Y)


ani1 = animation.ArtistAnimation(figure1, images, interval = 150)
ani1.save("/src/images/regression-gradient-decent.gif", writer = "imagemagick")

plot.plot(X, Y,"bo")
plot.plot([0, 10], [0 + bias1, 10 * weight1 + bias1], linewidth = 1.0, color = "g")
plot.savefig("/src/images/regression-gradient-decent.png")
