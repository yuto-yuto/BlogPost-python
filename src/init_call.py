from typing import Any


class InitCall:
    def __init__(self) -> None:
        print("__init__ was called")
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__ was called")

if __name__ == "__main__":
    instance = InitCall()
    instance()