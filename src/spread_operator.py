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
array_of_array = [array1, array2]
flatten_array = [*array1, *array2]

print(array_of_array)  # [[1, 2, 3, 4], [9, 8, 7, 6]]
print(flatten_array)  # [1, 2, 3, 4, 9, 8, 7, 6]

print("--- with asterisk ---")
print(*array_of_array)  # [1, 2, 3, 4] [9, 8, 7, 6]
print(*flatten_array)  # 1 2 3 4 9 8 7 6

flatten_array2 = [
    *array_of_array[0],
    *array_of_array[1],
]
print(flatten_array2)  # [1, 2, 3, 4, 9, 8, 7, 6]


def calc_sum(a, b, c, d):
    print(f"sum({a}, {b}, {c}, {d}):{a+b+c+d}")

calc_sum(*array1) # sum(1, 2, 3, 4):10