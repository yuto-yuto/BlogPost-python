from typing import Dict
from collections import defaultdict
import random

# print({1.1: 1})
# print(dict(1=1))
# print(dict(1.1=1))

print("----- Read -----")

def run():
    data_dict = {1: "Apple", 2: "Orange", 3: "Strawberry"}
    data_dict2 = dict(one="Apple", two="Orange")
    empty_dict1 = {}
    empty_dict2 = dict()
    # {1: 'Apple', 2: 'Orange', 3: 'Strawberry'}
    print(data_dict)
    print(data_dict2)

    # 1: Apple, 2: Orange, 3: Strawberry
    print(f"1: {data_dict[1]}, 2: {data_dict[2]}, 3: {data_dict[3]}")
    data_dict[4] = "Blueberry"
    print(data_dict)
    # {1: 'Apple', 2: 'Orange', 3: 'Strawberry', 4: 'Blueberry'}

    del data_dict[4]
    try:
        del data_dict[4]
    except KeyError as err:
        print(f"KeyError occurred. Key: {err}")

    for key in [1, 3, 4]:
        if key in data_dict:
            print(f"data_dict contains key {key}")
        else:
            print(f"data_dict doesn't contain key {key}")


def without_defaultdict():
    count_dict: Dict[int, int] = {}

    for num in range(10):
        num = int(random.random() * 5)
        if num not in count_dict:
            print(f"new key was created [{num}]")
            count_dict[num] = 0
        count_dict[num] += 1

    for key, value in count_dict.items():
        print(f"key: {key}, value: {value}")


def with_defaultdict():
    count_dict: Dict[int, int] = defaultdict(lambda : 5)

    for num in range(10):
        num = int(random.random() * 5)
        count_dict[num] += 1

    for key, value in count_dict.items():
        print(f"key: {key}, value: {value}")

# without_defaultdict()
with_defaultdict()
