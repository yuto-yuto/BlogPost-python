class FirstClass():
    _protected_one = 1
    __private_one = 1

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Destructor for FirstClass was called")
        self.name = None
        print(f"name was set to {self.name}")

    def return_hello(self):
        return f"Hello {self.name}"

    def use_members(self):
        print("protected: " + str(self._protected_one))
        print("private: " + str(self.__private_one))

    def do_something(self):
        raise NotImplementedError("Method not implemented")


instance = FirstClass("Yuto")
print(instance.return_hello())
print(instance._protected_one)
print(instance.use_members())
print(instance.__private_one)
print("---------")


class SecondClass(FirstClass):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)

    def __del__(self):
        print("Destructor for SecondClass was called")
        self.age = None
        print(f"age was set to {self.age}")
        super().__del__()

    def return_hey(self):
        return f"Hey {self.name} {self.age}"


instance2 = SecondClass("Yuto2", 35)
print(instance2.return_hello())
print(instance2.return_hey())

try:
    print("Call doSomething()")
    instance2.do_something()
except BaseException as e:
    print(f"ERROR: {e}")
