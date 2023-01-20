class MyException(Exception):
    def __init__(self):
        super().__init__("An error occurred for some reason")

class MyException2(MyException):
    def __init__(self, error_code):
        self.error_code = error_code
        # str(err) will output the following without this
        # MyException2: 55, error_code: 55
        super().__init__()


class TooColdException(Exception):
    def __init__(
        self,
        *,
        error_code=None,
        extra_msg=None,
    ):
        self.error_code = error_code
        self.extra_msg = extra_msg

        if error_code == 1:
            action = "Close all windows."
        elif error_code == 2:
            action = "Turn the heater on."
        else:
            action = "Wait for Summer."

        super().__init__(
            f"Too Cold Exception occurred.\n"
            f"Error code: {error_code}\n"
            f"Action: {action}\n"
            f"Extra_msg: {extra_msg}"
        )


errors = [
    MyException(),
    MyException2(55),
    Exception("Normal error"),
    TooColdException(),
    TooColdException(error_code=1),
    TooColdException(error_code=2, extra_msg="It is 22 degrees in the room though."),
    TooColdException(error_code=3),
]

for error in errors:
    try:
        raise error
    except TooColdException as err:
        print(f"TooColdException: {str(err)}")
        if err.error_code == 1:
            print("-----> I will close all windows later.")
        elif err.error_code == 2:
            print("-----> I will turn the heater on in 30 minutes.")
        else:
            print(f"-----> I don't know what to do for error code [{err.error_code}]")

    except MyException2 as err:
        print(f"MyException2: {str(err)}, error_code: {err.error_code}")
    except MyException as err:
        print(f"MyException: {str(err)}")
    except Exception as err:
        print(f"Exception: {str(err)}")
    print()
