data_array = [None, 0, 0.1, -1, 1, "", "hoge",
              [], [[]], [0], (), (0), (1), (0, 0), range(0)]

[print(f"value: {str(value).ljust(10)}, result: {not value}")
 for value in data_array]
