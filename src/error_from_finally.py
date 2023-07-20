from typing import List


def do_something(value: int):
    if value > 5:
        raise NameError(f"uncaught error from do_something. value: {value}")
    if value > 0:
        raise RuntimeError(f"error from do_something. value: {value}")
    print(f"do something. value: {value}")


def reset_state(value: int) -> None:
    if value > 0:
        raise ValueError("value must be bigger than 0")
    print("reset done")


def run_reset1(value: int):
    try:
        do_something(value)
    except RuntimeError as err:
        print(err)
    finally:
        reset_state(value)


class MultiExceptions(Exception):
    def __init__(self, errors: List[Exception]) -> None:
        self.errors = errors
        messages = ", ".join([f"{type(x)}: {str(x)}" for x in errors])
        super().__init__(messages)


def run_reset2(param: int):
    errors: List[Exception] = []
    try:
        do_something(param)
    except Exception as err:
        errors.append(err)

    try:
        reset_state(param)
    except Exception as err:
        errors.append(err)

    if len(errors) == 1:
        raise errors[0]
    if len(errors) > 1:
        raise MultiExceptions(errors)

    print("completed")


def catch_error1(value: int):
    try:
        run_reset1(value)
    except Exception as ex:
        print(ex)


def catch_error2(value: int):
    try:
        run_reset2(value)
    except MultiExceptions as ex:
        print(f"ERRORS: {ex}")
        if RuntimeError in ex.errors:
            print("RuntimeError is included.")
        for error in ex.errors:
            if isinstance(error, RuntimeError):
                print(f"RuntimeError: {error}")


# run_reset1(0)
# run_reset1(1)
# catch_error1(1)
# catch_error1(10)

catch_error2(0)
catch_error2(1)
