class CustomException(Exception):
    pass


class MyExceptionWithFixedMsg(Exception):
    def __init__(self):
        super().__init__("An error occurred for some reason")


class MyExtendedException(MyExceptionWithFixedMsg):
    def __init__(self, error_code):
        self.error_code = error_code
        # str(err) will output the following without this
        # MyException2: 55, error_code: 55
        super().__init__()

    def __str__(self):
        return f"MyExtendedException(error_code: {self.error_code})"


class MyExceptionWithParameters(Exception):
    def __init__(self, error_code):
        self.error_code = error_code
        super().__init__(
            f"MyExceptionWithParameters error message. error_code: {error_code}"
        )


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


def run0():
    try:
        raise Exception("Database is not ready")
        # raise  Exception("Unknown error")
    except Exception as err:
        if "Database is not ready" in str(err):
            print("wait for the initilization of the Database")
        else:
            print("unknown error")


def run1():
    try:
        raise CustomException("Database is not ready")
    except CustomException as err:
        print(f"error: {str(err)}")
        print("wait for the initilization of the Database")
    except Exception as err:
        print("unknown error")


def run2_():
    try:
        raise MyExtendedException(error_code=123)
    except MyExtendedException as err:
        print(f"error_code: {err.error_code}")
        print(f"str(err): {str(err)}")


def run2():
    errors = [
        MyExceptionWithFixedMsg(),
        MyExtendedException(55),
        Exception("Normal error"),
        TooColdException(),
        TooColdException(error_code=1),
        TooColdException(
            error_code=2, extra_msg="It is 22 degrees in the room though."
        ),
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
                print(
                    f"-----> I don't know what to do for error code [{err.error_code}]"
                )

        except MyExtendedException as err:
            print(f"MyExtendedException: {str(err)}, error_code: {err.error_code}")
        except MyExceptionWithFixedMsg as err:
            print(f"MyExceptionWithFixedMsg: {str(err)}")
        except Exception as err:
            print(f"Exception: {str(err)}")
        print()


def run3():
    try:
        try:
            raise MyExceptionWithParameters(999)
        except Exception as err:
            raise TooColdException(
                error_code=12,
                extra_msg="It's cold.",
            ) from err
    except TooColdException as error:
        print(f"error code: {error.error_code}")
        print(f"extra msg: {error.extra_msg}")
        print(f"str(error) >>> {str(error)}")
        print(f"str(error.__cause__) >>> {str(error.__cause__)}")
    except Exception as error:
        print(isinstance(error, Exception))  # True
        print(isinstance(error, MyExceptionWithParameters))  # False
        print(isinstance(error, TooColdException))  # True
