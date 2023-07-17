# import math
# import random

# # Определение средне арифметического значения массива
# def mean(a):
#     return sum(a) / len(a) # 45 / 9 = 5


# def deviation(arr):
#     arrMean = mean(arr)

#     sumOfDifferences = 0
#     for i in arr:
#         sumOfDifferences += (i - arrMean) ** 2

#     sumOfDifferences /= (len(arr) - 1)

#     return (sumOfDifferences) ** 0.5

# # Коэффциент корреляции
# def coefCorr(a, b):
#     sum = 0
#     n = len(a)
#     for i, j in zip(a, b):
#         sum += i * j
    
#     sum -= n * mean(a) * mean(b)

#     sum /= (n - 1) * deviation(a) * deviation(b)

#     return sum

# # mean: 90, 100, 3, 4
# # 
# #





# # Туалетная бумага, батарейки, лапша, лампочка
# # recommend = {
# #     'Саня': [5, 2, 3, 4],
# #     'Алеша': [1, 4, 2, 2],
# #     # ...
# #     'Кто-то': [5, 5, 5, -1],
# # }

# # row is order
# # Туалетная бумага, батарейки, лапша
# recommend = [
#     [1, 0, 1, 1, 1, 0, 1, 1],
#     [1, 0, 1, 1, 0, 1, 0, 1],
#     [0, 1, 1, 0, 0, 1, 0, 1]
# ]

# def distance(dataset, indOfInterest):
#     minSum = 10000000000
#     minIndex = -1

#     for i in range(len(dataset)):
#         sum = 0
#         if i != indOfInterest:
#             for j in range(len(dataset[i])):

#                 sum += (dataset[indOfInterest][j] - dataset[i][j])
#             if sum < minSum:
#                 minSum = sum
#                 minIndex = i

#     return minIndex

# print(distance(recommend, 1))



# X = [1.2, 2, 3, 4, 5, 6, 10, 16]
# Y = [3.001946414956816, 4.551200664306649, 4.425191057475725, 3.1022612673336543, 2.0592320059208635, 4.740320768388258, 1.6887564284017687, 3.954701796177326]

# print(X, Y)








# #       Chest, Waist, Legs, Height, Weight
# dataset = [
#     [     99,   56,    91,   160,    58],
#     [     89,   58,    89,   157,    48],
#     [     91,   64,    91,   165,    54],
#     [     91,   51,    91,   170,    54],
#     [     86,   56,    84,   157,    44],
#     [     97,   53,    86,   175,    56],
#     [     97,   53,    86,   175,    200]

# ]

# # A
# # Pi, i = 2
# # Pi(A) = 91
# restore = [94, 51, -1, 165, 54]

# def basicRegression(dataset, restoreObject):
#     columnNumber = len(dataset[0])
#     rowNumber = len(dataset)

#     meanArrays = []
#     columnArrays = []
#     indexOfAim = -1

#     for i in range(columnNumber):
#         columnArray = []
#         for j in range(rowNumber):
#             columnArray.append(dataset[j][i])

#         columnArrays.append(columnArray)
#         meanArrays.append(mean(columnArray))

#     for i in range(len(restoreObject)):
#         if restoreObject[i] == -1:
#             indexOfAim = i

    
#     print(meanArrays)

#     sum = 0
#     sumOfCorrelation = 0

#     for i in range(columnNumber):
#         if indexOfAim != i:
#             sumOfCorrelation += abs(coefCorr(columnArrays[indexOfAim], columnArrays[i]))
#             sum += coefCorr(columnArrays[indexOfAim], columnArrays[i]) * (restoreObject[i] - meanArrays[i])

#     return meanArrays[indexOfAim] + (sum / sumOfCorrelation)



# print(basicRegression(dataset, restore))

















# # def regression(dataset, restore):
# #     columnNumber = len(dataset[0])
# #     rowNumber = len(dataset)

# #     meanArray = []
# #     columnArrays = []

# #     for i in range(columnNumber):
# #         columnArray = []
# #         for j in range(rowNumber):
# #             columnArray.append(dataset[j][i])

# #         meanArray.append(mean(columnArray))
# #         columnArrays.append(columnArray)

# #     indOfRestore = -1
# #     for i in range(len(restore)):
# #         if restore[i] == -1:
# #             indOfRestore = i
# #             break

# #     sum = 0
# #     sumOfCorrelations = 0
# #     for i in range(columnNumber):
# #         if i != indOfRestore:
# #             sumOfCorrelations += abs(coefCorr(columnArrays[indOfRestore], columnArrays[i]))
# #             sum += coefCorr(columnArrays[indOfRestore], columnArrays[i]) * (restore[i] - meanArray[i])


# #     resValue = meanArray[indOfRestore] + (sum / sumOfCorrelations)
# #     return resValue

# # print(regression(dataset, restore))

    





























import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([
            [56,    91,   160,    58],
            [58,    89,   157,    48],
            [64,    91,   165,    54],
            [51,    91,   170,    54],
            [56,    84,   157,    44],
            [53,    86,   175,    56]])

Y = np.array([99, 89, 91, 91, 86, 97])
restore = np.array([[51, 91, 165, 54]])

# Step 3: Create an instance of LinearRegression
model = LinearRegression()

# Step 4: Fit the model to the data
model.fit(X, Y)

# Step 5: Predict using the trained model
predictions = model.predict(restore)
print(predictions)
