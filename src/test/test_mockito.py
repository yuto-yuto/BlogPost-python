from typing import List
import pytest
from mockito import matchers, mock, verify, when, when2, invocation, unstub


def sum_of(a, b):
    return a + b


@pytest.fixture(autouse=True)
def after():
    yield
    unstub()


class ForStub:
    def __init__(self):
        self.__val = 1

    def func1(self, param1: int, param2: int) -> int:
        return param1 + param2

    def func2(self) -> None:
        return

    def func3(self) -> int:
        return self.__val

    def __private_func(self) -> str:
        return "private string value"

    def func4(self) -> str:
        return self.__private_func()


def test1_func1():
    instance = ForStub()
    when(instance).func1(1, 1).thenReturn(3)

    assert 3 == instance.func1(1, 1)
    with pytest.raises(invocation.InvocationError):
        instance.func1(1, 2)


def test2_func1():
    instance = ForStub()
    when(instance).func1(...).thenReturn(3)

    assert 3 == instance.func1(1, 8)
    assert 3 == instance.func1(5, 5)


def test3_func1():
    when(ForStub).func1(1, 1).thenReturn(3)

    instance = ForStub()
    assert 3 == instance.func1(1, 1)


def test4_func1():
    instance = ForStub()
    when2(instance.func1, ...).thenReturn(3)

    assert 3 == instance.func1(1, 19)
    assert 3 == instance.func1(5, 5)


def test5_func1():
    instance = ForStub()
    when2(instance.func1, 1, 1).thenReturn(3)

    assert 3 == instance.func1(1, 1)
    with pytest.raises(invocation.InvocationError):
        instance.func1(9, 9)


def test1_func2():
    instance = ForStub()
    when(instance).func2().thenReturn()

    assert None == instance.func2()


def test2_func2():
    instance = ForStub()
    when(instance).func2().thenReturn(1, 2, 3, 4)

    assert 1 == instance.func2()
    assert 2 == instance.func2()
    assert 3 == instance.func2()
    assert 4 == instance.func2()


def test3_func2():
    instance = ForStub()
    when(instance).func2().thenReturn([1, 2], (3, 4), [5, 6])

    assert [1, 2] == instance.func2()
    assert (3, 4) == instance.func2()
    assert [5, 6] == instance.func2()


def test1_func3():
    instance = ForStub()
    with pytest.raises(AttributeError):
        instance.__val == 9876

    with pytest.raises(AttributeError):
        when2(instance.__val).thenReturn(33)

    assert 1 == instance.func3()


def test2_func3():
    instance = ForStub()
    # {'_ForStub__val': 1}
    print(instance.__dict__)
    instance._ForStub__val = 33  # type: ignore
    assert 33 == instance.func3()


def test1_func4():
    instance = ForStub()
    # {'_ForStub__val': 1}
    print(instance.__dict__)
    def stub_private_func():
        return "dummy value"

    instance._ForStub__private_func = stub_private_func  # type: ignore
    assert "dummy value" == instance.func4()

