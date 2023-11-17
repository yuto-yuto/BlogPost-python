from typing import Iterator, List


def innter_yield(value: int) -> Iterator[int]:
    try:
        print("yield 1")
        yield 1
        print("yield 2")
        yield 2

        if value < 5:
            print("raise")
            raise KeyError(f"value: {value}")

        print("yield 3")
        yield 3

        if value > 5:
            return
    finally:
        print("finally block")

    print("after try-except-finally in innter_yield")


def run1(param: int) -> Iterator[str]:
    try:
        result_iterator = innter_yield(param)
        yield "run1 - 1"
        for val in result_iterator:
            yield f"iterate: {val}"
            print(f"iterate innter_yield({param}): {val}")
        print(f"iterate innter_yield({param}) ends")
    finally:
        print("finally in run1")

    print("after try-except-finally in run1")


def run2(param: int):
    try:
        result_iterator = innter_yield(param)
        for val in result_iterator:
            print(f"iterate innter_yield(param): {val}")
        print(f"iterate innter_yield({param}) ends")
    except StopIteration:
        print("StopIteration error")
    finally:
        print("finally in run2")

    print("after try-except-finally in run2")


def run3(param: int):
    try:
        result_iterator = innter_yield(param)
        for val in result_iterator:
            print(f"iterate innter_yield({param}): {val}")
        print("iterate innter_yield({param}) ends")
    except StopIteration:
        print("StopIteration error")
    except KeyError:
        print("Caught KeyError")
    finally:
        print("finally in do_yield4_2")

    print("after try-except-finally in do_yield4_2")


def reset_state(value: int) -> None:
    if value <= 0:
        raise ValueError("value must be bigger than 0")
    print("reset done")


def run_reset1(param: int):
    try:
        result_iterator = innter_yield(param)
        for val in result_iterator:
            print(f"iterate innter_yield({param}): {val}")
        print("iterate innter_yield({param}) ends")
    except StopIteration:
        print("Caught StopIteration")
    finally:
        reset_state(param)


class MultiExceptions(Exception):
    def __init__(self, errors: List[Exception]) -> None:
        self.errors = errors
        messages = ", ".join([f"{type(x)}: {str(x)}" for x in errors])
        super().__init__(messages)


def run_reset2(param: int):
    errors: List[Exception] = []
    try:
        result_iterator = innter_yield(param)
        for val in result_iterator:
            print(f"iterate innter_yield({param}): {val}")
        print("iterate innter_yield({param}) ends")
    except StopIteration:
        print("Caught StopIteration")
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

try:
    run_reset2(10)
except Exception as err:
    print(err)

# try:
#     run_reset1(1)
# except Exception as err:
#     print(err)