import timeit

class Pair:
    def __init__(self, val) -> None:
        self.value1 = val
        self.value2 = str(val)

SIZE = 99999

pairs = []
tuples = []
my_dict = {}
array_list= []

for i in range(SIZE):
    pairs.append(Pair(i))
    tuples.append((i,str(i)))
    my_dict[i] = str(i)
    array_list.append([i,str(i)])

def run_pairs():
    for pair in pairs:
        a = pair.value1
        b = pair.value2

def run_tuples():
    for tuple in tuples:
        a = tuple[0]
        b = tuple[1]

def run_dict1():
    for key, value in my_dict.items():
        a = key
        b = value
        
def run_dict2():
    for key in my_dict.keys():
        a = key
        b = my_dict[key]

def run_array_list():
    for array in array_list:
        a = array[0]
        b = array[1]

LOOP_COUNT = 10
print(timeit.timeit("run_pairs()", "from __main__ import run_pairs", number=LOOP_COUNT))    # 0.12340559999938705
print(timeit.timeit("run_tuples()", "from __main__ import run_tuples", number=LOOP_COUNT))  # 0.10513519999949494
print(timeit.timeit("run_dict1()", "from __main__ import run_dict1", number=LOOP_COUNT))    # 0.06451990000095975
print(timeit.timeit("run_dict2()", "from __main__ import run_dict2", number=LOOP_COUNT))    # 0.08417579999877489
print(timeit.timeit("run_array_list()", "from __main__ import run_array_list", number=LOOP_COUNT))  # 0.11757700000089244

