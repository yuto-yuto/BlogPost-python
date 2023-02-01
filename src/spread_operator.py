import json
import datetime

# class Position:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.items = [x, y]

# objArray = [
#     Position(1,1),
#     Position(2,1),
#     Position(3,1),
# ]

# items = [
#     objArray[0],
#     objArray[1],
# ]

array1 = [1, 2, 3, 4]
array2 = [9, 8, 7, 6]
arrayOfArray = [array1, array2]

print("--- *arrayOfArray ---")
print(*arrayOfArray)
print("--- **arrayOfArray ---")

a = [
    *arrayOfArray[0],
    *arrayOfArray[1],
]
print(datetime.datetime.now())
