from typing import Any, List, Optional, Type, TypeVar, Union


def cast(val: Any) -> Type[Union[int, str, bool, None]]:
    if isinstance(val, str):
        return str
    elif isinstance(val, bool):
        return bool
    elif isinstance(val, int):
        return int
    else:
        return type(None)


print(cast("abc"))  # <class 'str'>
print(cast(122))    # <class 'int'>
print(cast(True))   # <class 'bool'>
print(isinstance(True, int))    # True
print(isinstance(False, int))   # True
print(cast(["abc", 122]))       # None


T = TypeVar("T")


def is_str_list(val: List[Any]) -> bool:
    return all(isinstance(x, str) for x in val)


def is_int_list(val: List[Any]) -> bool:
    return all(isinstance(x, int) for x in val)


def str_list(val: List[Any]) -> Optional[List[str]]:
    is_mix = any(not isinstance(i, str) for i in val)

    if is_mix:
        return None

    return val


def int_list(val: List[Any]) -> Optional[List[int]]:
    is_mix = any(not isinstance(i, int) for i in val)

    if is_mix:
        return None

    return val


def same_type_list(val: List[Any]) -> Optional[List[Any]]:
    first_type = type(val[0])
    is_mix = any(not isinstance(i, first_type) for i in val)

    if is_mix:
        return None

    return val


# def return_list(val: List[Any]) -> Union[List[int], List[str]]:
#     values = list(map(cast, val))
#     if is_str_list(values):
#         return values
#     elif is_int_list(values):
#         return values
#     # raise Exception("Error")
#     return values

# def return_list(val: List[Any]) -> Union[List[int], List[str]]:
#     result = str_list(val)
#     if result:
#         return result

#     result = int_list(val)
#     if result:
#         return result

#     raise Exception("Error")

def return_list(val: List[Any]) -> Union[List[int], List[str]]:
    result = same_type_list(val)
    if result:
        return result

    raise Exception("Error")


print(return_list(["11", "22"]))
print(return_list([11, 22]))
print(return_list([11, "22"]))
