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

def set_value2(obj):
    obj.my_obj.a = 1
    obj.my_obj.b = 2

obj = MyClass1()
print(obj.a)
print(obj.b)
print(obj.my_obj.aa)
print(obj.my_obj.bb)

set_value2(obj)
print(obj.my_obj.aa)
print(obj.my_obj.bb)
