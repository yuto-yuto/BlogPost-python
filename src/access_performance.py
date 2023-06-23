from typing import List
import timeit
from collections import namedtuple

KeyValueTuple = namedtuple('KeyValueTuple', ["k", "v"])
# KeyValueTuple = namedtuple('KeyValueTuple', "k v")


class Pair:
    def __init__(self, val) -> None:
        self.value1 = val
        self.value2 = str(val)


SIZE = 99999

pairs = []
tuples = []
key_value_tuples: List[KeyValueTuple] = []
my_dict = {}
array_list = []

for i in range(SIZE):
    pairs.append(Pair(i))
    tuples.append((i, str(i)))
    key_value_tuples.append(KeyValueTuple(i, str(i)))
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


def run_named_tuples():
    for tuple in key_value_tuples:
        a = tuple.k
        b = tuple.v


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
print(timeit.timeit("run_pairs()", "from __main__ import run_pairs", number=LOOP_COUNT))                    
print(timeit.timeit("run_pairs_getattr()", "from __main__ import run_pairs_getattr", number=LOOP_COUNT))    
print(timeit.timeit("run_tuples()", "from __main__ import run_tuples", number=LOOP_COUNT))                  
print(timeit.timeit("run_named_tuples()", "from __main__ import run_named_tuples", number=LOOP_COUNT))
print(timeit.timeit("run_dict_items()", "from __main__ import run_dict_items", number=LOOP_COUNT))          
print(timeit.timeit("run_dict_keys()", "from __main__ import run_dict_keys", number=LOOP_COUNT))            
print(timeit.timeit("run_dict_list_dict()", "from __main__ import run_dict_list_dict", number=LOOP_COUNT))  
print(timeit.timeit("run_dict_list_items()", "from __main__ import run_dict_list_items", number=LOOP_COUNT))
print(timeit.timeit("run_array_list()", "from __main__ import run_array_list", number=LOOP_COUNT))          

# PC1
# run_pairs           | 0.1270339000002422 | 0.12103550099982385 | 0.1205554100006338
# run_pairs_getattr   | 0.2222416000004159 | 0.18320076200052426 | 0.2053344470004958
# run_tuples          | 0.0931681000001845 | 0.09771581199947832 | 0.1063894089993482
# run_named_tuples    |                    |                     |       
# run_dict_items      | 0.0592193999982555 | 0.05689544600045337 | 0.0650553529994795
# run_dict_keys       | 0.0833707000001595 | 0.07583839899962186 | 0.0873097409994443
# run_dict_list_dict  | 0.1133616999995865 | 0.08741327899952012 | 0.1128004120000696
# run_dict_list_items | 0.2255674000007275 | 0.22594992500035005 | 0.3004420150000442
# run_array_list      | 0.1156945000002451 | 0.09885911899982602 | 0.1573325290000866

# PC2
# run_pairs           | 0.1872 | 0.1888 | 0.1935 | 0.2631
# run_pairs_getattr   | 0.2964 | 0.3164 | 0.2835 | 0.4495
# run_tuples          | 0.1286 | 0.1256 | 0.1332 | 0.1666
# run_named_tuples    | 0.1635 | 0.1628 | 0.1558 | 0.2104
# run_dict_items      | 0.1353 | 0.1302 | 0.1292 | 0.1723
# run_dict_keys       | 0.1664 | 0.1680 | 0.1638 | 0.2220
# run_dict_list_dict  | 0.1759 | 0.1792 | 0.1755 | 0.2427
# run_dict_list_items | 0.2620 | 0.2612 | 0.2671 | 0.3267
# run_array_list      | 0.1337 | 0.1315 | 0.1352 | 0.1768