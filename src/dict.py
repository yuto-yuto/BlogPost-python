import re

data = {
    "0\\price": 1.5,
    "0\\name": "Apple",
    "0\\stock": 50,
    "1\\price": 1.2,
    "1\\name": "Orange",
    "1\\stock": 22,
    "2\\price": 1100.4,
    "2\\name": "nice-pc",
    "2\\stock": 5,
}

[print(f"{key}, {data[key]}") for key in data]
print(data.keys())
print(data.values())
print(data.items())

# data_list = [{key: value} for key, value in data.items()]
# print(data_list)

for key in data.keys():
    result = re.search("(\d+)", key)
    if result:
        print(f"{result}  -> {result.group(1)}")
    else:
        print("Not found")

result = re.search("(\d+) (\d+ .+)", "111 222 333")
if result:
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))

for key in data.keys():
    result = re.search("(\d+)\\\\(.+)", key)
    if result:
        print(f"key: {result.group(1)}, value: {result.group(2)}")
    else:
        print("Not found")

restructure = {}
last_base_key = None
for key, value in data.items():
    result = re.search("(\d+)\\\\(.+)", key)
    if not result:
        raise Exception("Unexpected format")

    index = result.group(1)
    key = result.group(2)
    if index != last_base_key:
        restructure[index] = {}
    last_base_key = index
    restructure[index][key] = value

print(restructure)

print("------------")


def restructure_dict(dict, reg_str):
    result = {}
    last_base_key = None
    for key, value in data.items():
        search_result = re.search(reg_str, key)
        if not search_result:
            raise Exception("Unexpected format found: {key}")

        index = search_result.group(1)
        key = search_result.group(2)
        if index != last_base_key:
            result[index] = {}
        last_base_key = index
        result[index][key] = value
    return result

data = {
    "apple:prop1": "1-1",
    "apple:prop2": "1-2",
    "apple:prop3": "1-3",
    "apple:prop4": None,
    "honey:prop1": "2-1",
    "honey:prop2": "2-2",
    "honey:prop3": "2-3",
    "juice:prop1": "3-1",
    "juice:prop2": "3-2",
    "juice:prop3": "3-3",
}
restructed_data = restructure_dict(data, "(.+):(.+)")
print(restructed_data)

print(restructed_data["apple"]["prop1"])
print(restructed_data["apple"])
print(restructed_data["apple"].pop("prop1"))
print(restructed_data["apple"].pop("prop4"))
print(restructed_data["apple"].pop("unknown", None))
print(restructed_data["apple"])
