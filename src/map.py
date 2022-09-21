
def power(val):
    return val * val


result = map(power, [1, 2, 3])
print(result)
# <map object at 0x00000174CF1D5FA0>
print([print(v) for v in result])
# 1
# 4
# 9
# [None, None, None]
print(list(result))  # []

print()
result = map(power, [1, 2, 3])
print(f"list(result): {list(result)}")

print()


def multiply(val, val2):
    return val * val2


result = map(multiply, [1, 2, 3, 4], [2, 3, 4, 5])
print(list(result))  # [2, 6, 12, 20]

result = map(multiply, [1, 2, 3, 4], [1, 1])
print(list(result))  # [1, 2]

print(list(map(lambda val: val * val, [1, 2, 3])))
# [1, 4, 9]
