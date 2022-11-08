class MyData:
    def __init__(self) -> None:
        self.my_prop1 = "initial 1"
        self.my_prop2 = "initial 2"
        self.my_prop3 = "initial 3"
        self.my_prop4 = "initial 4"


def fetch_data():
    return {
        "prop1": "value1",
        "prop2": None,
        "prop3": "value3",
        "prop4": "value4",
    }


source_dict = fetch_data()
data = MyData()

val = source_dict.pop("prop1", None)
if val is not None:
    data.my_prop1 = val

val = source_dict.pop("prop2", None)
if val is not None:
    data.my_prop2 = val

val = source_dict.pop("prop3", None)
if val is not None:
    data.my_prop3 = val

val = source_dict.pop("prop4", None)
if val is not None:
    data.my_prop4 = val

print(f"prop1: {data.my_prop1}")
print(f"prop2: {data.my_prop2}")
print(f"prop3: {data.my_prop3}")
print(f"prop4: {data.my_prop4}")


class MyClass1:
    def __init__(self) -> None:
        self.a = 33
        self.b = 55
        self.my_obj = MyClass2()


class MyClass2:
    def __init__(self) -> None:
        self.aa = 99
        self.bb = 88
        pass


def set_value(obj):
    obj.a = 1
    obj.b = 2
    obj.my_obj.aa = 9999
    obj.my_obj.bb = 8888


def set_value_but_error(obj, key):
    obj[key] = 1


def set_value2(obj, key, value):
    if value is not None:
        setattr(obj, key, value)


def set_value3(obj, key, value):
    if value is None:
        return

    if hasattr(obj, key):
        setattr(obj, key, value)


obj = MyClass1()
print(f"obj.a: {obj.a}")
print(f"obj.b: {obj.b}")
print(f"obj.my_obj.aa: {obj.my_obj.aa}")
print(f"obj.my_obj.bb: {obj.my_obj.bb}")

print("--- set_value1 ---")
set_value(obj)
print(f"obj.a: {obj.a}")
print(f"obj.b: {obj.b}")
print(f"obj.my_obj.aa: {obj.my_obj.aa}")
print(f"obj.my_obj.bb: {obj.my_obj.bb}")

# set_value_but_error(obj, "a")

print("--- set_value2 ---")
obj2 = MyClass1()
set_value2(obj2, "a", 22)
set_value2(obj2, "b", None)
set_value2(obj2, "not_exist", 55)

print(f"obj2.a: {obj2.a}")
print(f"obj2.b: {obj2.b}")
print(f"obj2.not_exist: {obj2.not_exist}")

print("--- set_value3 ---")
obj3 = MyClass1()
set_value3(obj3, "a", 1000)
set_value3(obj3, "b", None)
set_value3(obj3, "not_defined", 6000)

print(f"obj3.a: {obj3.a}")
print(f"obj3.b: {obj3.b}")
try:
    print(f"obj3.not_exist: {obj3.not_defined}")
except Exception as err:
    print(format(err))

print("\n improved ---- ")
source_dict = fetch_data()
data = MyData()
for key, value in source_dict.items():
    set_value3(data, f"my_{key}", value)

print(f"prop1: {data.my_prop1}")
print(f"prop2: {data.my_prop2}")
print(f"prop3: {data.my_prop3}")
print(f"prop4: {data.my_prop4}")

print("\n improved with predefined dict ---- ")
source_dict = fetch_data()
data = MyData()
mapping_dict = {
    "my_prop1": "prop1",
    "my_prop2": "prop2",
    "my_prop3": "prop3",
    "my_prop4": "prop4",
}
for new_key, original_key in mapping_dict.items():
    set_value3(data, new_key, source_dict.pop(original_key, None))

print(f"prop1: {data.my_prop1}")
print(f"prop2: {data.my_prop2}")
print(f"prop3: {data.my_prop3}")
print(f"prop4: {data.my_prop4}")
