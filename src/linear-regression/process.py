import without_bias
import with_bias

# import matplotlib.pyplot as plot
# import matplotlib.animation as animation
# import numpy as np
# import seaborn as sns

# def calculateLoss(X, Y, weight, bias = 0):
#     predictedLine = X * weight + bias
#     return np.average((predictedLine - Y) ** 2)

# def train(X, Y):
#     weight = 0
#     learningRate = 100
#     for i in range(1000):
#         if i % 10 == 0:
#             plot.plot(X, Y, "bo")
#             image = plot.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
#             images.append(image)

#         currentLoss = calculateLoss(X, Y, weight)
#         print(i, currentLoss)
#         if currentLoss > calculateLoss(X, Y, weight + learningRate):
#             weight += learningRate
#         elif currentLoss > calculateLoss(X, Y, weight - learningRate):
#             weight -= learningRate
#         else:
#             return weight
#     return weight


# def gradient(X, Y, weight, bias):
#     predictedLine = X * weight + bias
#     return 2 * np.average(X * (predictedLine - Y))


# def trainWithBias(X, Y):
#     weight = 14019946383
#     bias = 0
#     learningRate = 0.1
#     for i in range(1000000):
#         if i % 200 == 0:
#             plot.plot(X, Y, "bo")
#             image = plot.plot([0, 10], [0, 10 * weight + bias], linewidth = 1.0, color = "g")
#             biasImages.append(image)
#         currentLoss = calculateLoss(X, Y, weight, bias)
#         loss1 = calculateLoss(X, Y, weight + learningRate, bias)
#         loss2 = calculateLoss(X, Y, weight - learningRate, bias)
#         loss3 = calculateLoss(X, Y, weight, bias + learningRate)
#         loss4 = calculateLoss(X, Y, weight, bias - learningRate)

#         minLoss = min(currentLoss, loss1, loss2, loss3, loss4)
#         print(i, currentLoss)
#         if minLoss == loss1:
#             weight += learningRate
#         elif minLoss == loss2:
#             weight -= learningRate
#         elif minLoss == loss3:
#             bias += learningRate
#         elif minLoss == loss4:
#             bias -= learningRate
#         else:
#             return (weight, bias)

#     return (weight, bias)


# data = np.genfromtxt('./dataset/housing.csv', delimiter = ',', skip_header = 1)
# X = data[:, 0]
# Y = data[:, 3]

# figure1 = plot.figure(1)
# figure2 = plot.figure(2)
# figure3 = plot.figure(3)
# figure4 = plot.figure(4)
# fig1 = figure1.add_subplot(1, 1, 1)
# fig2 = figure2.add_subplot(1, 1, 1)
# fig3 = figure3.add_subplot(1, 1, 1)
# fig4 = figure4.add_subplot(1, 1, 1)
# images = []

# weight = train(X, Y)

# sns.set()
# plot.xticks(fontsize = 10)
# plot.yticks(fontsize = 10)
# plot.xlabel("RM", fontsize = 10)
# plot.ylabel("MEDV", fontsize = 10)

# fig1.plot(X, Y,"bo")
# fig1.plot([0, 10], [0, 10 * weight], linewidth = 1.0, color = "g")
# figure1.savefig("/src/images/linear-regression-without-bias.png")

# print(images)
# ani1 = animation.ArtistAnimation(figure2, images, interval = 100)
# ani1.save("/src/images/regression.gif", writer = "imagemagick")

# # biasImages = []
# # weightWithBias = trainWithBias(X, Y)

# # fig3.plot(X, Y,"bo")
# # fig3.plot([0, 10], [0, 10 * weightWithBias[0] + weightWithBias[1]], linewidth = 1.0, color = "g")
# # figure3.savefig("/src/images/linear-regression-with-bias.png")

# # ani2 = animation.ArtistAnimation(figure4, biasImages, interval = 10)
# # ani2.save("/src/images/regression-with-bias.gif", writer = "imagemagick")
