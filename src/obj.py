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
set_value2(obj, "a", 22)
set_value2(obj, "b", None)
set_value2(obj, "not_exist", 55)

print(f"obj.a: {obj.a}")
print(f"obj.b: {obj.b}")
print(f"obj.not_exist: {obj.not_exist}")

print("--- set_value3 ---")
set_value3(obj, "a", 1000)
set_value3(obj, "b", None)
set_value3(obj, "not_defined", 6000)

print(f"obj.a: {obj.a}")
print(f"obj.b: {obj.b}")
print(f"obj.not_exist: {obj.not_defined}")