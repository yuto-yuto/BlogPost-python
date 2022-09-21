from traceback import print_tb


data = [1, 2, 3, 4]
data.insert(0, 0)
print(data)  # [0, 1, 2, 3, 4]

data = [1, 2, 3, 4]
data.insert(0, [-2, -1])
print(data)  # [[-2, -1], 1, 2, 3, 4]

data = [1, 2, 3, 4]
data[:0] = [-2, -1]
print(data)  # [-2, -1, 1, 2, 3, 4]

data = [1, 2, 3, 4]
data[0:] = [-2, -1]
print(data)  # [-2, -1]

print()

data = [1, 2, 3, 4]
print(data[0])   # 1
print(data[0:])  # [1, 2, 3, 4]
print(data[2:])  # [3, 4]
print(data[3:])  # [4]
print(data[-1:])  # [4]
print(data[-2:])  # [3, 4]

print()

print(data[:0])  # []
print(data[:2])  # [1, 2]
print(data[:3])  # [1, 2, 3]
print(data[:-1])  # [1, 2, 3]
print(data[:-2])  # [1, 2]

print()

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data[3: 7])  # [4, 5, 6, 7]

data = [1, 2, 3, 4]
data[:0] = [-1, -2, 0]
print(data)  # [-1, -2, 0, 1, 2, 3, 4]

data = [1, 2, 3, 4]
data[:2] = [-1, -2, 0]
print(data)  # [-1, -2, 0, 3, 4]

data = [1, 2, 3, 4]
data.append(5)
print(data)  # [1, 2, 3, 4, 5]

data = [1, 2, 3, 4]
data.append([5, 6])
print(data)  # [1, 2, 3, 4, [5, 6]]

data = [1, 2, 3, 4]
data.insert(len(data), 5)
print(data)  # [1, 2, 3, 4, 5]

data = [1, 2, 3, 4]
data.insert(len(data), [5, 6])
print(data)  # [1, 2, 3, 4, [5, 6]]

data = [1, 2, 3, 4]
data.extend([5, 6])
print(data)  # [1, 2, 3, 4, 5, 6]

print()
data = [1, 2, 3, 4]
print(data[0:]) # [1, 2, 3, 4]
data[0:] = [-1, -2, 0]
print(data)  # [-1, -2, 0]

data = [1, 2, 3, 4]
print(data[2:]) # [3, 4]
data[2:] = [-1, -2, 0]
print(data)  # [1, 2, -1, -2, 0]
print()

data = [1, 2, 3, 4, 5, 6, 7]
print(data[1:2])
data[1:2] = [99, 100]
print(data)  # [1, 2, -1, -2, 0]

data = [1, 2, 3, 4, 5, 6, 7]
print(data[1:6])
data[1:6] = [99, 100]
print(data)  # [1, 2, -1, -2, 0]
