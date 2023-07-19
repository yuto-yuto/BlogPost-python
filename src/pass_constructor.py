from typing import Iterator, Generic, Union, Type, TypeVar


class FooReturnType:
    def __init__(self, value):
        self.value = value
        self.name = "FOO"
        self.foo_val = 123


class BarReturnType:
    def __init__(self, value):
        self.value = value
        self.name = "BAR"
        self.bar_val = 998


class Foo:
    def __init__(self, value: int):
        self.value = value

    def execute(self) -> FooReturnType:
        return FooReturnType(self.value)


class Bar:
    def __init__(self, value: int):
        self.value = value

    def execute(self) -> BarReturnType:
        return BarReturnType(self.value)


def create_instance(create: Union[Type[Foo], Type[Bar]]) -> Union[Foo, Bar]:
    return create(30)


def run1():
    foo = Foo(10)
    result = foo.execute()
    print(f"{result.name}, {result.foo_val}, {result.value}")
    # FOO, 123, 10

    bar = Bar(20)
    result = bar.execute()
    print(f"{result.name}, {result.bar_val}, {result.value}")
    # BAR, 998, 20


def run2():
    foo = create_instance(Foo)

    if isinstance(foo, Foo):
        result = foo.execute()
        print(f"{result.name}, {result.foo_val}, {result.value}")
        # FOO, 123, 30

    result = foo.execute()
    print(f"{result.name}, {result.foo_val}, {result.value}")
    # FOO, 123, 30


T = TypeVar("T", Foo, Bar)


def create_instance2(create: Type[T]) -> T:
    return create(30)


def run3():
    foo = create_instance2(Foo)

    if isinstance(foo, Foo):
        result = foo.execute()
        print(f"{result.name}, {result.foo_val}, {result.value}")

    result = foo.execute()
    print(f"{result.name}, {result.foo_val}, {result.value}")


class FooBar(Generic[T]):
    def __init__(self, create: Type[T]) -> None:
        self._create = create

    def execute(self) -> Iterator[T]:
        print("---Hello from FooBar")
        for i in range(1, 3):
            yield self._create(i + i)


# def run4():
#     foo = FooBar(Foo)
#     for val in foo.execute():
#         result =val.execute()
#     # ---Hello from FooBar
#     # Hello from Foo

#     bar = FooBar(Bar)
#     bar.execute()
#     # ---Hello from FooBar
#     # Hello from Bar


class Service:
    def execute_foofoo(self):
        foobar = FooBar(Foo)
        for foo in foobar.execute():
            result = foo.execute()
            print(f"{result.name}, {result.foo_val}, {result.value}")

    def execute_barbar(self):
        foobar = FooBar(Bar)
        for bar in foobar.execute():
            result = bar.execute()
            print(f"{result.name}, {result.bar_val}, {result.value}")


def run5():
    service = Service()
    service.execute_foofoo()
    # ---Hello from FooBar
    # FOO, 123, 2
    # FOO, 123, 4

    service.execute_barbar()
    # ---Hello from FooBar
    # BAR, 998, 2
    # BAR, 998, 4


print("--- 1 ---")
run1()
print("--- 2 ---")
run2()
print("--- 3 ---")
run3()
print("--- 4 ---")
# run4()
print("--- 5 ---")
run5()
