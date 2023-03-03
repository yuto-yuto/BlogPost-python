print("--- string to float ---")
print(float("15"))  # 15.0
print(float("15.99"))  # 15.99

print("--- string to int ---")
print(int("15"))  # 15.0
try:
    print(int("15.99"))
except ValueError as err:
    print(err)
print(int(float("15.99")))

print(int("11", 2))  # 3
print(int("11", 10))  # 11
print(int("11", 16))  # 17
print(int("FF", 16))  # 255

print("--- string to int ---")
print(str(11))  # 11
print(str(11.123))  # 11.123

print("--- list to string ---")
list1 = [1, 2, 3, 4, 5]
print(str(list1))  # [1, 2, 3, 4, 5]
listMap = map(str, list1)
print(",".join(listMap))  # 1,2,3,4,5

print("--- dict to string ---")
dict1 = {"key1": 11, "key2": 22, "key3": 33}
print(str(dict1))  # {'key1': 11, 'key2': 22, 'key3': 33}

print("--- dict keys to string ---")
print(str(dict1.keys()))  # dict_keys(['key1', 'key2', 'key3'])
keyMap = map(str, dict1.keys())
print(list(keyMap))  # ['key1', 'key2', 'key3']

keyMap = map(str, dict1.keys())
print(",".join(keyMap))  # key1,key2,key3

print("--- dict values to string ---")
print(str(dict1.values()))  # dict_values([11, 22, 33])

valueMap = map(str, dict1.values())
print(list(valueMap))  # ['11', '22', '33']

valueMap = map(str, dict1.values())
print(",".join(list(valueMap)))  # 11,22,33


class MyClassA:
    def __init__(self, *, name, speed, private_prop, protedted_prop):
        self.name = name
        self.speed = speed
        self._protedted_value = protedted_prop
        self.__private_value = private_prop

    def __str__(self):
        return f"name: {self.name}, speed: {self.speed}, protected: {self._protedted_value}, private: {self.__private_value}"


myClassA = MyClassA(
    name="name A",
    speed=50,
    protedted_prop="protected value",
    private_prop="private value",
)

print(str(myClassA))  # <__main__.MyClassA object at 0x7fb1b59c7ee0>
# name: name A, speed: 50, protected: protected value, private: private value