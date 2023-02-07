class MyClass:
    def __init__(self):
        self.public1 = 1
        self.public2 = "value 2"
        self._protected1 = 3
        self._protected2 = "value 4"
        self.__private1 = 5
        self.__private2 = "value 6"

    def public_method(self):
        print("I'm a public method")

    def _protected_method(self):
        print("I'm beautiful protected method")

    def __private_method(self):
        print("I'm a dirty private method")


obj = MyClass()
for prop, val in vars(obj).items():
    print(f"prop: {prop}, value: {val}")
