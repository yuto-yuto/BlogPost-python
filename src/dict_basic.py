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
