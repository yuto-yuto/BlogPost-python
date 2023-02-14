from typing import Dict

list_1 = [8, 2, 47, 3, 9, 1, 234, 8, 342, 21]
list_of_list = [[1, 2, 4], [6, 9, 1], [2, 1, 5], [5, 3, 22, 57]]


def filter_with_loop():
    result1 = []
    for item in list_1:
        if item > 10:
            result1.append(item)
    print(result1)

    result2 = []
    for item_list in list_of_list:
        if max(item_list) > 5:
            result2.append(item_list)
    print(result2)


print("--- filter_with_loop ---")
filter_with_loop()


def filter_with_lambda():
    result1 = filter(lambda a: a > 10, list_1)
    # [47, 234, 342, 21]
    print(list(result1))

    result2 = filter(lambda data_list: max(data_list) > 5, list_of_list)
    # [[6, 9, 1], [5, 3, 22, 57]]
    print(list(result2))


print("--- filter_with_lambda ---")
filter_with_lambda()


def filter_with_func():
    def bigger_than_10(val):
        return val > 10

    result1 = filter(bigger_than_10, list_1)
    # [47, 234, 342, 21]
    print(list(result1))

    def contains_number_bigger_than_5(data_list):
        return max(data_list) > 5

    result2 = filter(contains_number_bigger_than_5, list_of_list)
    # [[6, 9, 1], [5, 3, 22, 57]]
    print(list(result2))


print("--- filter_without_lambda ---")
filter_with_func()

data_dict: Dict[str, float] = {
    "aaa": 1.0,
    "bbb": 2.2,
    "ccc": 3.2,
    "ddd": 5.5,
    "eee": 8.0,
}


def show_dict():
    # Consider iterating with .items()
    for key in data_dict:
        print(f"{key}, {data_dict[key]}")

    for pair in data_dict.items():
        key, value = pair
        print(f"{pair[0]}, {pair[1]} \t{key}, {value}")


show_dict()
# aaa, 1.0        aaa, 1.0
# bbb, 2.2        bbb, 2.2
# ccc, 3.2        ccc, 3.2
# ddd, 5.5        ddd, 5.5
# eee, 8.0        eee, 8.0


def dict_filter(pair):
    _key, value = pair
    return value > 3


# {'ccc': 3.2, 'ddd': 5.5, 'eee': 8.0}
print(dict(filter(lambda pair: pair[1] > 3, data_dict.items())))
# {'ccc': 3.2, 'ddd': 5.5, 'eee': 8.0}
print(dict(filter(dict_filter, data_dict.items())))
# {}
print(dict(filter(lambda pair: pair[1] > 30, data_dict.items())))


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


points = [
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
    Point(4, 4),
    Point(5, 5),
]

for point in points:
    print(f"({point.x}, {point.y})")
# (1, 1)
# (2, 2)
# (3, 3)
# (4, 4)
# (5, 5)

print("--- after filter ---")
points = filter(lambda point: point.x > 3, points)

for point in points:
    print(f"({point.x}, {point.y})")
# (4, 4)
# (5, 5)
