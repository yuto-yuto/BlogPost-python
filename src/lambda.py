print("--- fn1 ---")
fn = lambda: print("Hello World!")
fn()
# Hello World!

print("--- fn2 ---")
fn2 = lambda x, y, z: print(f"(x, y, z): ({x}, {y}, {z})")
fn2(11, 22, 33)
# (x, y, z): (11, 22, 33)

print("--- fn3 ---")
fn3 = lambda x, *args, y, **kwargs: print(
    f"x: {x}, args: {args}, y: {y}, kwargs: {kwargs}"
)
fn3(11, 12, 13, 14, y=55, example_arg1=1, example_arg2=22)
# x: 11, args: (12, 13, 14), y: 55, kwargs: {'example_arg1': 1, 'example_arg2': 22}

print("--- fn4 ---")
fn4 = lambda found: print("found") if found else print("not found")
fn4(True)  # found
fn4(False)  # not found

print("--- fn5 ---")
fn5 = lambda x: [res := x + x, res := res + res + x, print(res)]
fn5(1)  # 5

print("--- fn6 ---")
fn6 = lambda data: [data := [3, 4], data := [data[0] + data[1]], print(data)]
data = [1, 2]
fn6(data)
print(data)
# [7]
# [1, 2]


def update_list_data(data):
    data[0] = 11


update_list_data(data)
print(data)
# [11, 2]

print("--- map ---")
data_list = [1, 2, 3, 4, 5]
result = map(lambda x: x * x, data_list)
print(list(result))
# [1, 4, 9, 16, 25]

print("--- sort ---")
data_list2 = [("AAA", 35), ("BBB", 12), ("CCC", 92), ("DDD", 22)]
data_list2.sort(key=lambda data: data[1])
print(data_list2)
# [('BBB', 12), ('DDD', 22), ('AAA', 35), ('CCC', 92)]
