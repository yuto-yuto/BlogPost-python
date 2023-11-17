import pytest
from mockito import matchers, when, when2, invocation, spy2, unstub, verify


def sum_of(a, b):
    return a + b


@pytest.fixture(autouse=True)
def after():
    yield
    unstub()


class DataChangeDetector:
    def trigger_callback(self, trigger, callback):
        if trigger:
            callback(1, 2)


class ForStub:
    def __init__(self, detector=DataChangeDetector()):
        self.__val = 1
        self.__detector = detector

    def func1(self, param1: int, param2: int) -> int:
        return param1 + param2

    def func1_name(self, *, param1: int, param2: int) -> int:
        return self.func1(param1, param2)

    def func2(self) -> None:
        return

    def func3(self) -> int:
        return self.__val

    def __private_func(self) -> str:
        return "private string value"

    def func4(self) -> str:
        return self.__private_func()

    def func5(self, trigger, callback) -> None:
        self.__detector.trigger_callback(trigger, callback)

    def func6(self, trigger, callback) -> None:
        def on_changed(values: list[int]):
            if len(values) == 1:
                callback(values[0])
            else:
                callback(",".join(map(str, values)))

        if trigger:
            on_changed([1, 2, 3, 4])


def test1_func1():
    instance = ForStub()
    when(instance).func1(1, 1).thenReturn(3)
    when(instance).func1(5, 1).thenReturn(99)

    assert 3 == instance.func1(1, 1)
    assert 99 == instance.func1(5, 1)

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
    instance2 = ForStub()
    assert 3 == instance2.func1(1, 1)


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


def test4_func2():
    instance = ForStub()
    when(instance).func2().thenReturn(1).thenReturn(5).thenReturn(8)

    assert 1 == instance.func2()
    assert 5 == instance.func2()
    assert 8 == instance.func2()


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
    # private string value
    print(instance.func4())

    def stub_private_func():
        return "dummy value"

    instance._ForStub__private_func = stub_private_func  # type: ignore
    assert "dummy value" == instance.func4()


def test1_func5():
    instance = ForStub()
    value = [0]

    def callback(a, b):
        value[0] = a + b

    instance.func5(True, callback)
    assert value[0] == 3


def test2_func5():
    instance = ForStub()
    value = [0]

    def callback(a, b):
        value[0] = a + b

    instance.func5(False, callback)
    assert value[0] == 0


def test3_func5():
    detector = DataChangeDetector()
    instance = ForStub(detector)
    value = [0]

    def callback(a, b):
        value[0] = a + b

    when(detector).trigger_callback(...).thenAnswer(lambda a, b: callback(5, 5))
    instance.func5(False, callback)
    assert value[0] == 10


def test4_func5():
    detector = DataChangeDetector()
    instance = ForStub(detector)

    captor = matchers.captor()
    when(detector).trigger_callback(False, captor)

    value = [0]

    def callback(a, b):
        value[0] = a + b

    instance.func5(False, callback)

    callback_in_trigger_callback = captor.value

    callback_in_trigger_callback(1, 1)
    assert value[0] == 2
    callback_in_trigger_callback(3, 3)
    assert value[0] == 6


def test1_func6():
    instance = ForStub()

    def verify_callback(updated_value):
        assert updated_value == "1,2,3,4"

    instance.func6(True, verify_callback)


def test1_verify_with_spy2():
    instance = ForStub()
    spy2(instance.func1)
    instance.func1(1, 1)
    instance.func1(2, 2)
    verify(instance, atleast=1).func1(...)
    verify(instance, times=2).func1(...)
    verify(instance, atleast=1).func1(1, 1)
    verify(instance, atleast=1).func1(2, 2)

    # Error
    # verify(instance, times=2).func1(1, 1)


def test2_verify_with_spy2():
    instance = ForStub()
    spy2(instance.func1_name)
    instance.func1_name(param1=1, param2=1)
    instance.func1_name(param1=2, param2=2)
    verify(instance, times=2).func1_name(...)
    verify(instance, atleast=1).func1_name(param1=1, param2=1)
    verify(instance, atleast=1).func1_name(param1=2, param2=2)


def test_verify_with_when():
    instance = ForStub()
    when(instance).func1(...).thenReturn(5)
    instance.func1(1, 1)
    instance.func1(2, 2)
    verify(instance, atleast=1).func1(...)
    verify(instance, times=2).func1(...)
    verify(instance, atleast=1).func1(1, 1)
    verify(instance, atleast=1).func1(2, 2)
