empty_dict1 = {}
empty_dict2 = dict()
print(f"empty_dict1: {isinstance(empty_dict1, dict)}, {empty_dict1}")
print(f"empty_dict2: {isinstance(empty_dict2, dict)}, {empty_dict2}")

data_dict = {1: "Apple", 2: "Orange", 3: "Strawberry"}
data_dict2 = dict(one="Apple", two="Orange")
# {1: 'Apple', 2: 'Orange', 3: 'Strawberry'}
print(data_dict)
# {'one': 'Apple', 'two': 'Orange'}
print(data_dict2)

# print({1.1: 1})
# print(dict(1=1))
# print(dict(1.1=1))

print("----- Read -----")

# 1: Apple, 2: Orange, 3: Strawberry
print(f"1: {data_dict[1]}, 2: {data_dict[2]}, 3: {data_dict[3]}")
# one: Apple, two: Orange
print(f"one: {data_dict2['one']}, two: {data_dict2['two']}")
print(f"1: {data_dict.get(1)}")

try:
    print(data_dict[999])
except KeyError as err:
    print(f"KeyError: {err}")
print(f"1: {data_dict.get(999)}")
print(f"1: {data_dict.get(999, 'default-value 999')}")

print("----- Add -----")

data_dict[4] = "Blueberry"
print(data_dict)
# {1: 'Apple', 2: 'Orange', 3: 'Strawberry', 4: 'Blueberry'}

print("----- Update -----")

data_dict[4] = "Rasberry"
print(data_dict)
data_dict.update({1: "Green Apple", 4: "Riped Rasberry", 5: "Something", 6: "Empty"})
# {1: 'Green Apple', 2: 'Orange', 3: 'Strawberry', 4: 'Riped Rasberry', 5: 'Something', 6: 'Empty'}
print(data_dict)

print(data_dict2)
data_dict2.update({"eight": "value 8"}, nine="value 9", ten="value 10")
print(data_dict2)

print("----- Delete -----")
try:
    print(data_dict)
    del data_dict[4]
    print(data_dict)
    del data_dict[4]
except KeyError as err:
    print(f"KeyError occurred. Key: {err}")

print(data_dict)
pop_data = data_dict.pop(6)
print(pop_data)
print(data_dict)
pop_data = data_dict.pop(99999, "DEFAULT-VALUE")
print(pop_data)

print("--- popitem ---")
data_dict3 = dict(one="value1", two="value2", three="value3", four="value4")
print(data_dict3.popitem())
print(data_dict3)
data_dict3.popitem()
data_dict3.popitem()
data_dict3.popitem()
print(data_dict3)
try:
    data_dict3.popitem()
except Exception as err:
    print(err)

print("----- Copy and Delete all -----")
copied_dict = data_dict.copy()
print(data_dict)
data_dict.clear()
print(data_dict)

print("----- Check key existance -----")
for key in [1, 3, 4]:
    if key in copied_dict:
        print(f"data_dict contains key {key}")
    else:
        print(f"data_dict doesn't contain key {key}")

print("----- Get first -----")
# {1: 'Green Apple', 2: 'Orange', 3: 'Strawberry', 5: 'Something', 6: 'Empty'}
print(copied_dict)
# 1
print(list(copied_dict.keys())[0])
# Green Apple
print(list(copied_dict.values())[0])
# (1, 'Green Apple')
print(list(copied_dict.items())[0])
