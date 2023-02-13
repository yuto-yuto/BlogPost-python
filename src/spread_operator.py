from typing import Any, List

print("-----")

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

print("--- plus operator / extend ---")
print(array_of_array[0] + array_of_array[1])  # [1, 2, 3, 4, 9, 8, 7, 6]
array_of_array[0].extend(array_of_array[1])
print(array_of_array[0])  # [1, 2, 3, 4, 9, 8, 7, 6]
print(array1)  # [1, 2, 3, 4, 9, 8, 7, 6]
print(flatten_array)  # [1, 2, 3, 4, 9, 8, 7, 6]
print(flatten_array2)  # [1, 2, 3, 4, 9, 8, 7, 6]

print("--- flatten ---")
nested_arrays = [[1, 2, 3], [4, 5], [6, [7, [8, 9]]]]


def flatten(array: List[Any]):
    result = []
    for item in array:
        result.extend(item)
    return result


def recursive_flatten(array: List[Any]):
    result = []
    for item in array:
        if isinstance(item, list):
            result.extend(recursive_flatten(item))
        else:
            result.append(item)
    return result


print(flatten(nested_arrays))  # [1, 2, 3, 4, 5, 6, [7, [8, 9]]]
print(recursive_flatten(nested_arrays))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


def calc_sum(a, b, c, d):
    print(f"sum({a}, {b}, {c}, {d}):{a+b+c+d}")


calc_sum(*[1, 2, 3, 4])  # sum(1, 2, 3, 4):10
params = [1, 2, 3, 4, 5]
# Too many positional arguments for function call
# calc_sum(*params)
calc_sum(*params[0:4])  # sum(1, 2, 3, 4):10
calc_sum(*params[1:5])  # sum(2, 3, 4, 5):14
calc_sum(*params[-4:])  # sum(2, 3, 4, 5):14

print("--- dict ---")
data_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
}
print(*data_dict)  # one two three
print(" ".join(data_dict.keys()))  # one two three


array_from_dict = [*data_dict]
set_from_dict = {*data_dict}
print(array_from_dict)  # ['one', 'two', 'three']
print(isinstance(set_from_dict, set))  # True
print(set_from_dict)  # {'one', 'three', 'two'}
print(set_from_dict.pop())  # one

dict_from_dict = {**data_dict}
print(isinstance(dict_from_dict, dict))  # True
# {'one': 1, 'two': 2, 'three': 33, 'four': 4}
print({**dict_from_dict, "four": 4, "three": 33})
# {'four': 4, 'three': 3, 'one': 1, 'two': 2}
print({"four": 4, "three": 33, **data_dict})
