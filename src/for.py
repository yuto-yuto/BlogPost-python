for num in [22, 33, 44, 55]:
    print(num)
else:
    print(f"Last number is {num}")

for char in "Hello":
    print(char)

for element in ([1, 2, 3], "Hello", 5, ("key", "value")):
    print(element)

print()
print(list(range(5, 15)))
print(list(range(5, 15, 2)))
print()

for num in range(5):
    print(num)

print()
[print(num) for num in range(5)]
new_list = [num * num for num in range(5)]
print(new_list)

[
    print(num * num)
    for num
    in range(5)
]

print()


print()
array = [[1, 11], [2, 22], [3, 33]]
for i, k in array:
    print(f"i: {i}, k: {k}")

print()
for key_value in array:
    print(f"i: {key_value[0]}, k: {key_value[1]}")

print()
for i, [key, value] in enumerate(array):
    print(f"i: {i}, [{key}, {value}]")

print()
lower_cases = ["a", "b", "c"]
lower_cases2 = [c for c in lower_cases]
print(lower_cases is lower_cases)   # True
print(lower_cases is lower_cases2)  # False
print(lower_cases == lower_cases2)  # True
