class FirstClass():
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Destructor for FirstClass was called")
        self.name = None
        print(f"name was set to {self.name}")

    def ReturnHello(self):
        return f"Hello {self.name}"

    def doSomething(self):
        raise NotImplementedError("Method not implemented")


instance = FirstClass("Yuto")
print(instance.ReturnHello())
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

    def ReturnHey(self):
        return f"Hey {self.name} {self.age}"


instance2 = SecondClass("Yuto2", 35)
print(instance2.ReturnHello())
print(instance2.ReturnHey())

try:
    print("Call doSomething()")
    instance2.doSomething()
except BaseException as e:
    print(f"ERROR: {e}")
