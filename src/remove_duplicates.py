from typing import List

duplicated_int_list = [1, 2, 3, 4, 2, 3, 4, 5]


def remove_with_for(data_list: List[int]):
    result = []
    for item in data_list:
        if item not in result:
            result.append(item)
    return result


print(remove_with_for(duplicated_int_list))
# [1, 2, 3, 4, 5]


def remove_with_set(data_list: List[int]):
    return list(set(data_list))


print(remove_with_set(duplicated_int_list))
# [1, 2, 3, 4, 5]


def remove_with_from_keys(data_list: List[int]):
    keys = dict.fromkeys(data_list)
    # {1: None, 2: None, 3: None, 4: None, 5: None}
    print(keys)
    return list(keys)


print(remove_with_from_keys(duplicated_int_list))


def remove_with_comparing_index(data_list: List[int]):
    result = []
    for index, item in enumerate(data_list):
        if index == data_list.index(item):
            result.append(item)
    return result


print(remove_with_comparing_index(duplicated_int_list))


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


print("---- remove duplicated object----")
duplicated_points = [
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
    Point(4, 4),
    Point(2, 2),
    Point(6, 3),
    Point(4, 4),
    Point(5, 5),
]
print(Point(1, 1) == Point(1, 1))  # False


def show_points(points: List[Point]):
    for point in points:
        print(f"({point.x}, {point.y})")


def equal_point(a: Point, b: Point):
    return a.x == b.x and a.y == b.y


def remove_object_for(points: List[Point]):
    result: List[Point] = []
    for current in points:
        found = False
        for stored in result:
            if equal_point(current, stored):
                found = True
        if found is False:
            result.append(current)
    return result


print("--- remove_object_for ---")
show_points(remove_object_for(duplicated_points))


def remove_object_enumerate(points: List[Point]):
    def index_where(data_list: List[Point], search: Point):
        for index, item in enumerate(data_list):
            if equal_point(item, search) is True:
                return index
        return -1

    result: List[Point] = []
    for index, current in enumerate(points):
        if index == index_where(points, current):
            result.append(current)

    return result


print("--- remove_object_enumerate ---")
show_points(remove_object_enumerate(duplicated_points))
