import timeit


class Pair:
    def __init__(self, val) -> None:
        self.value1 = val
        self.value2 = str(val)


SIZE = 99999

pairs = []
tuples = []
my_dict = {}
array_list = []

for i in range(SIZE):
    pairs.append(Pair(i))
    tuples.append((i, str(i)))
    my_dict[i] = str(i)
    array_list.append([i, str(i)])


def run_pairs():
    for pair in pairs:
        a = pair.value1
        b = pair.value2

def run_pairs_getattr():
    for pair in pairs:
        a = getattr(pair, "value1")
        b = getattr(pair, "value2")


def run_tuples():
    for tuple in tuples:
        a = tuple[0]
        b = tuple[1]


def run_dict_items():
    for key, value in my_dict.items():
        a = key
        b = value


def run_dict_keys():
    for key in my_dict.keys():
        a = key
        b = my_dict[key]


def run_dict_list_dict():
    for key in list(my_dict):
        a = key
        b = my_dict[key]


def run_dict_list_items():
    for pair in list(my_dict.items()):
        a = pair[0]
        b = pair[1]


def run_array_list():
    for array in array_list:
        a = array[0]
        b = array[1]


# fmt: off
LOOP_COUNT = 10
print(timeit.timeit("run_pairs()", "from __main__ import run_pairs", number=LOOP_COUNT))                    # 0.12703390000024228
print(timeit.timeit("run_pairs_getattr()", "from __main__ import run_pairs_getattr", number=LOOP_COUNT))    # 0.22224160000041593
print(timeit.timeit("run_tuples()", "from __main__ import run_tuples", number=LOOP_COUNT))                  # 0.0931681000001845
print(timeit.timeit("run_dict_items()", "from __main__ import run_dict_items", number=LOOP_COUNT))          # 0.05921939999825554
print(timeit.timeit("run_dict_keys()", "from __main__ import run_dict_keys", number=LOOP_COUNT))            # 0.08337070000015956
print(timeit.timeit("run_dict_list_dict()", "from __main__ import run_dict_list_dict", number=LOOP_COUNT))  # 0.11336169999958656
print(timeit.timeit("run_dict_list_items()", "from __main__ import run_dict_list_items", number=LOOP_COUNT))# 0.2255674000007275
print(timeit.timeit("run_array_list()", "from __main__ import run_array_list", number=LOOP_COUNT))          # 0.11569450000024517


