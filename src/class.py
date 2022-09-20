

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
# print(instance.__private_one)
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


def abstract_class1():
    class Person():
        def __init__(self, name, age):
            self._name = name
            self._age = age

        def work(self):
            raise NotImplementedError("Method not implemented")

        def greet(self):
            raise NotImplementedError("Method not implemented")

    class Developer(Person):
        def work(self):
            print("I'm developing something...")

        def greet(self):
            print(f"Hi, I'm a developer. Name: {self._name}, Age: {self._age}")

    class Manager(Person):
        def work(self):
            print("I'm creating a plan...")

        def greet(self):
            print(f"Hi, I'm a manager. Name: {self._name}, Age: {self._age}")

    Person("Yuto", 35)
    from typing import List
    persons: List[Person] = [Developer("Yuto", 35), Manager("TOTO", 55)]
    for instance in persons:
        instance.greet()
        instance.work()


print("---------abstract_class1-------")
abstract_class1()


def abstract_class2():

    from abc import ABC, abstractmethod

    class Person(ABC):
        def __init__(self, name, age):
            self._name = name
            self._age = age

        @abstractmethod
        def work(self):
            pass

        @abstractmethod
        def greet(self):
            pass

    class Developer(Person):
        def work(self):
            print("I'm developing something...")

        def greet(self):
            print(f"Hi, I'm a developer. Name: {self._name}, Age: {self._age}")

    class Manager(Person):
        def work(self):
            print("I'm creating a plan...")

        def greet(self):
            print(f"Hi, I'm a manager. Name: {self._name}, Age: {self._age}")

    # Error
    # Person("Yuto", 35)
    from typing import List
    persons: List[Person] = [Developer("Yuto", 35), Manager("TOTO", 55)]
    for instance in persons:
        instance.greet()
        instance.work()


print("---------abstract_class2-------")
abstract_class2()


class A():
    def hello(self):
        return "hello from A"

    def boo(self):
        return "boo"


class B():
    def hello(self):
        return "hello from B"

    def beeee(self):
        return "beeee"


class C(A, B):
    pass


print("----- multi inheritances ----")
instance = C()
print(instance.hello())
print(instance.boo())
print(instance.beeee())

print("---- END ----")
