from typing import List, Union

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
# [1, 2, 3, 4, 5]


def remove_with_comparing_index(data_list: List[int]):
    result = []
    for index, item in enumerate(data_list):
        if index == data_list.index(item):
            result.append(item)
    return result


print(remove_with_comparing_index(duplicated_int_list))
# [1, 2, 3, 4, 5]


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class PointEx(Point):
    def __eq__(self, __o: object) -> bool:
        return self.x == getattr(__o, "x", None) and self.y == getattr(__o, "y", None)

    def __hash__(self) -> int:
        return hash(("x", self.x, "y", self.y))

    def equal_with(self, __o: object, *keys: str) -> bool:
        if isinstance(__o, PointEx) is False:
            return False

        if len(keys) == 0:
            return True

        for key in keys:
            if getattr(self, key) != getattr(__o, key):
                return False
        return True


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


def show_points(points: Union[List[Point], List[PointEx]]):
    for point in points:
        print(f"({point.x}, {point.y})")


def equal_point(a: Point, b: Point):
    return a.x == b.x and a.y == b.y


print("--- remove_object_set ---")
show_points(list(set(duplicated_points)))
print(Point(4, 4).__eq__(Point(4, 4)))

print("--- remove_object_set with __eq__ ---")
duplicated_pointExes = [
    PointEx(1, 1),
    PointEx(2, 2),
    PointEx(3, 3),
    PointEx(4, 4),
    PointEx(2, 2),
    PointEx(6, 3),
    PointEx(4, 4),
    PointEx(5, 5),
]
print(PointEx(4, 4).__eq__(PointEx(4, 4)))
print(PointEx(4, 4) == PointEx(4, 4))
show_points(list(set(duplicated_pointExes)))

print("--- remove_object_for ---")


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


def remove_object_for2(points: List[PointEx]):
    result: List[PointEx] = []
    for current in points:
        found = False
        for stored in result:
            if current == stored:
                found = True
        if found is False:
            result.append(current)
    return result


def remove_object_for3(points: List[PointEx]):
    result: List[PointEx] = []
    for current in points:
        if current not in result:
            result.append(current)
    return result


def remove_object_for_partial(points: List[PointEx]):
    result: List[PointEx] = []
    for current in points:
        found = False
        for stored in result:
            if current.equal_with(stored, "y"):
                found = True
        if found is False:
            result.append(current)
    return result


show_points(remove_object_for(duplicated_points))
print("--- remove_object_for2 ---")
show_points(remove_object_for2(duplicated_pointExes))
print("--- remove_object_for3 ---")
show_points(remove_object_for3(duplicated_pointExes))
print("--- remove_object_for_partial ---")
show_points(remove_object_for_partial(duplicated_pointExes))


print("--- remove_object_enumerate ---")


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


show_points(remove_object_enumerate(duplicated_points))
