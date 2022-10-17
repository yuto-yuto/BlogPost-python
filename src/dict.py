data = {
    "0\\val1": 0.0,
    "0\\val2": "STRING-VALUE",
    "0\\val3": 5,
    "1\\val1": 0.2,
    "1\\val2": "STRING-VALUE222",
    "1\\val3": 22,
    "2\\val1": 3.3,
    "2\\val2": "STRING-VALUE333",
    "2\\val3": 333,
}

[print(f"{key}, {data[key]}") for key in data]
print(data.keys())
print(data.values())
print(data.items())

data_list = [{key: value} for key, value in data.items()]
print(data_list)
