import timeit
from typing import Dict
from types import SimpleNamespace
from functools import partial

COUNT = 100000


def loop_append():
    result = []
    for i in range(1, COUNT):
        if i % 3 == 0:
            result.append(i)

    return len(result)


def map_append():
    result = []

    def handle(value):
        if value % 3 == 0:
            result.append(value)

    map(handle, range(1, COUNT))

    return len(result)


def _generate_dict():
    return {f"key_{i}": f"value_{i}" for i in range(0, COUNT)}


def loop_item(data: Dict[str, str]):
    result = SimpleNamespace()
    for i in range(COUNT * 5):
        key = f"key_{i}"
        value = data.pop(key, None)
        if value is not None:
            setattr(result, key, value)

    return result


def map_item(data: Dict[str, str]):
    result = SimpleNamespace()

    def handle(i: int):
        key = f"key_{i}"
        value = data.pop(key, None)
        if value is not None:
            setattr(result, key, value)

    map(handle, range(COUNT * 5))
    return result


print(timeit.timeit(loop_append, number=100))
print(timeit.timeit(map_append, number=100))
print(timeit.timeit(lambda: loop_item(_generate_dict()), number=10))
print(timeit.timeit(lambda: map_item(_generate_dict()), number=10))
