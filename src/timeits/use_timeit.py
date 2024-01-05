import timeit
from pathlib import Path
from random import randrange

def func1():
    return 1


def func2(a: int, b: int):
    return a + b


print(timeit.timeit(func1))
print(timeit.timeit(func1, number=100))
print(timeit.repeat(func1, repeat=5, number=100))
print(timeit.timeit(lambda: func2(randrange(100), randrange(100)), number=100))


def call_func2():
    a = randrange(100)
    b = randrange(100)
    func2(a + a, a - b)


print(timeit.timeit(call_func2, number=100))

print(timeit.repeat(call_func2, repeat=10, number=100))

filepath = Path(__file__).parent.joinpath("main.py")
print("hello_world.py 1: ", timeit.timeit("", "import hello_world", number=100))
print("hello_world.py 2: ", timeit.timeit("hello_world.hello()", "import hello_world", number=1))
print("hello_world.py 3: ", timeit.timeit("import hello_world", number=1))

print("hello_world.py 4: ", timeit.timeit("hello()", "from hello_world import hello", number=1))
print("hey.py: ", timeit.timeit("hey()", "from sub.hey import hey", number=1))

elapsed_time_second = timeit.timeit(
    f"hello_world.hello()", "import hello_world", number=1
)
elapsed_time_ms = elapsed_time_second * 1000
elapsed_time_micros = elapsed_time_ms * 1000
elapsed_time_ns = elapsed_time_micros * 1000
print(
    f"{format(elapsed_time_second,'.3f')} sec, "
    f"{format(elapsed_time_ms, '.3f')} ms, "
    f"{format(elapsed_time_micros,'.3f')} micro sec, "
    f"{format(elapsed_time_ns,'.3f')} ns"
)
