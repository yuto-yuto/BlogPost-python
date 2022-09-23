from typing import Any, List, Optional, Type, TypeVar, Union

print(type("sss"))  # <class 'str'>
print(type(123))    # <class 'int'>
print(type(True))   # <class 'bool'>
print(type([1, 2]))  # <class 'list'>

print(type("SSS") == str)  # True


class MyClass:
    pass


instance = MyClass()

print(type(instance) == MyClass)  # True

print()


def typeof(val: Any) -> Type[Union[int, str, bool, None]]:
    if isinstance(val, str):
        return str
    elif isinstance(val, bool):
        return bool
    elif isinstance(val, int):
        return int
    else:
        return type(None)


print(typeof("abc"))  # <class 'str'>
print(typeof(122))    # <class 'int'>
print(typeof(True))   # <class 'bool'>
print(isinstance(True, int))    # True
print(isinstance(False, int))   # True
print(typeof(["abc", 122]))       # None

print(list(map(int, [True, False])))


def is_str_list(val: List[Any]) -> bool:
    if len(val) == 0:
        return False
    return all(isinstance(x, str) for x in val)


def is_int_list(val: List[Any]) -> bool:
    if len(val) == 0:
        return False
    return all(isinstance(x, int) for x in val)


print("--- is_str_list ---")
print(is_str_list([]))  # False
print(is_str_list([1, 2, 3]))  # False
print(is_str_list(["1", 2]))  # False
print(is_str_list(["1", "2"]))   # True

print("--- is_int_list ---")
print(is_int_list([]))  # False
print(is_int_list([1, 2, 3]))  # True
print(is_int_list(["1", 2]))  # False
print(is_int_list(["1", "2"]))   # False


def process_list(values: Union[List[int], List[str], List[int | str]]) -> None:
    if is_str_list(values):
        for x in values:
            # IDE doesn't recognize that there is only one data type in the list
            pass


def str_list(val: List[Any]) -> Optional[List[str]]:
    is_mix = any(not isinstance(i, str) for i in val)

    if is_mix:
        return None

    return val


print()
print(str_list([]))  # []
print(str_list([1, 2, 3]))  # None
print(str_list(["1", 2]))   # None
print(str_list(["1", "2"]))  # ['1', '2']


def int_list(val: List[Any]) -> Optional[List[int]]:
    is_mix = any(not isinstance(i, int) for i in val)

    if is_mix:
        return None

    return val


def same_type_list(val: List[Any]) -> Union[List[int], List[str]]:
    result = int_list(val)
    if result:
        return result
    
    result = str_list(val)
    if result:
        return result
    raise Exception("The specified list has mixed data type")


def return_list(val: List[Any]) -> Union[List[int], List[str]]:
    if is_str_list(val):
        return val
    elif is_int_list(val):
        return val
    raise Exception("The specified list has mixed data type")


def return_list2(val: List[Any]) -> Union[List[int], List[str]]:
    result = str_list(val)
    if result:
        return result

    result = int_list(val)
    if result:
        return result

    raise Exception("The specified list has mixed data type")


def process_list2(values: Union[List[int], List[str], List[int | str]]) -> None:
    val = str_list(values)
    if val:
        for x in val:
            # IDE doesn't recognize that there is only one data type in the list
            pass

def return_list3(val: List[Any]) -> Union[List[int], List[str], List[bool]]:
    result = same_type_list(val)
    if result:
        return result

    raise Exception("The specified list has mixed data type")


print(return_list3(["11", "22"]))
print(return_list3([11, 22]))
try:
    print(return_list3([11, "22"]))
except Exception as err:
    print(err)

